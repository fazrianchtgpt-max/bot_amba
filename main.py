import discord
from discord.ext import commands, tasks
import sqlite3
import os
import re
from dotenv import load_dotenv
import google.generativeai as genai
import datetime
import asyncio
import fallback_templates
import keep_alive

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Initialize Google Gemini AI if API Key exists
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
else:
    model = None

SYSTEM_PROMPT = """
Kamu adalah Mas Amba yang romantis dan genit. Pelanggaran kata kunci jomok SUDAH TERKONFIRMASI oleh sistem.
Tugas kamu sekarang HANYA HANYA menyusun pesan balasan berupa rayuan manis dan kata-kata manja.

Instruksi Mutlak:
1. LANGSUNG berikan balasan berupa 'Surat Tanda Cinta Amba' (SPA). Sistem SUDAH MEMASTIKAN pelanggaran terjadi. JANGAN PERNAH MENOLAK ATAU MENGHARAPKAN KATA KUNCI DI PESAN!
2. Generate balasan yang romantis, menggoda (flirty). (Contoh: "Aduh Mas, deg-degan loh", "Mas kok gemesin banget sih").
3. Jangan pernah menulis nama asli target. Selalu gunakan format tag (misal: `<@12345678>`) yang diberikan di prompt.

Gaya Bahasa: Bahasa Indonesia santai, super romantis, manja. Panggil target dengan kata "Mas" lalu diikuti oleh Tag Panggilan sistem.
"""

SYSTEM_PROMPT_JUMAT = """
Kamu adalah Mas Amba. Ingat, hari ini adalah HARI JUMAT! Buang sifat genitmu! Berubah jadi tegas dan agamis.
Pelanggaran maksiat SUDAH TERKONFIRMASI oleh sistem. Tugas kamu sekarang LANGSUNG menceramahi target agar tobat.

Instruksi Mutlak:
1. LANGSUNG berikan balasan berupa 'Surat Peringatan Jumat Amba'. Sistem SUDAH MEMASTIKAN pelanggaran terjadi. JANGAN mengecek kata kunci lagi.
2. DILARANG KERAS memberikan komentar meta seperti "(tidak ada kata kunci)" atau semacamnya! Tulis kerangka marahmu saja.
3. Generate balasan berisi nasihat keras, ingatkan tentang dosa, neraka, murka Allah. Dilarang merayu, gombal.
4. Jangan pernah menulis nama asli target. Selalu gunakan format tag (misal: `<@12345678>`).

Gaya Bahasa: Sangat serius, bahasa Indonesia baku dicampur kosa kata Islami. Dilarang romantis. Panggil target dengan nama dari Tag Panggilan sistem.
"""

# Database Setup Using SQLite
def setup_db():
    conn = sqlite3.connect('amba.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS violations
                 (user_id TEXT PRIMARY KEY, username TEXT, points INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS keywords (word TEXT PRIMARY KEY)''')
    
    # Check if table is empty
    c.execute("SELECT count(*) FROM keywords")
    if c.fetchone()[0] == 0:
        default_keywords = ['jomok', 'ngawi', 'amba', 'rusdi', 'azril', 'zril', 'gay', 'homo', 'ahh', 'crt', 'crot', 'keluar', 'basah']
        for kw in default_keywords:
            c.execute("INSERT INTO keywords (word) VALUES (?)", (kw.lower(),))
            
    conn.commit()
    conn.close()

def get_keywords():
    conn = sqlite3.connect('amba.db')
    c = conn.cursor()
    c.execute("SELECT word FROM keywords")
    data = [row[0] for row in c.fetchall()]
    conn.close()
    return data

def add_keyword_db(word):
    conn = sqlite3.connect('amba.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO keywords (word) VALUES (?)", (word.lower(),))
        conn.commit()
        success = True
    except sqlite3.IntegrityError:
        success = False
    conn.close()
    return success

def remove_keyword_db(word):
    conn = sqlite3.connect('amba.db')
    c = conn.cursor()
    c.execute("DELETE FROM keywords WHERE word=?", (word.lower(),))
    deleted = c.rowcount > 0
    conn.commit()
    conn.close()
    return deleted

def add_violation(user_id, username):
    conn = sqlite3.connect('amba.db', timeout=10.0)
    c = conn.cursor()
    c.execute("""
        INSERT INTO violations (user_id, username, points) 
        VALUES (?, ?, 1)
        ON CONFLICT(user_id) DO UPDATE SET 
            points = violations.points + 1,
            username = excluded.username
    """, (user_id, username))
    
    c.execute("SELECT points FROM violations WHERE user_id=?", (user_id,))
    current_points = c.fetchone()[0]
    
    conn.commit()
    conn.close()
    return current_points

def get_leaderboard():
    conn = sqlite3.connect('amba.db')
    c = conn.cursor()
    c.execute("SELECT user_id, username, points FROM violations ORDER BY points DESC LIMIT 10")
    data = c.fetchall()
    conn.close()
    return data

# Discord Bot Setup
class AmbaBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)

    async def setup_hook(self):
        # Sync slash commands
        await self.tree.sync()

bot = AmbaBot()
# Task Reset Leaderboard Mingguan
@tasks.loop(hours=168) # 168 jam = 7 hari
async def weekly_reset():
    conn = sqlite3.connect('amba.db')
    c = conn.cursor()
    c.execute("DELETE FROM violations")
    conn.commit()
    conn.close()
    print("Leaderboard mingguan telah berhasil di-reset!")

@bot.event
async def on_ready():
    setup_db()
    
    # Jalankan jadwal reset mingguan jika belum jalan
    if not weekly_reset.is_running():
        weekly_reset.start()
        
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('Bot Mas Amba telah bersabda...')
    print('------')

@bot.event
async def on_message(message):
    if message.author.bot or message.content.startswith('/') or message.content.startswith('!'):
        return

    content_lower = message.content.lower()
    keywords = get_keywords()
    
    # Cek apakah hari ini hari Jumat (weekday 4 = Jumat)
    hari_jumat = datetime.datetime.now().weekday() == 4
    
    # Deteksi pelanggaran menggunakan Regex Boundary (\b) agar tidak mendeteksi di dalam kata (misal 'lahh' untuk 'ahh')
    if keywords:
        pattern = re.compile(r'\b(' + '|'.join(map(re.escape, keywords)) + r')\b')
        keyword_detected = pattern.search(content_lower)
    else:
        keyword_detected = False

    if keyword_detected:
        # Jika user ngetag target, masukkan pelanggaran ke target pertama. Jika tidak, masuk ke yang ngetik.
        target_user = None
        if message.mentions:
            for u in message.mentions:
                if not u.bot:
                    target_user = u
                    break
                    
        if target_user is None:
            target_user = message.author
            
        current_points = add_violation(str(target_user.id), str(target_user.name))
        
        is_reported = target_user.id != message.author.id
        
        # Penyesuaian Prompt dan Fallback berdasarkan hari
        if hari_jumat:
            active_prompt = SYSTEM_PROMPT_JUMAT
            if is_reported:
                fallback_msg = fallback_templates.get_jumat_reported(target_user.id, message.author.id, current_points)
                extra_instruction = f"- Target dilaporkan oleh <@{message.author.id}>. Beri tahu target secara keras bahwa dia dilaporkan oleh orang tersebut, lalu lanjutkan dengan teguran jumat."
            else:
                fallback_msg = fallback_templates.get_jumat_self(target_user.id, current_points)
                extra_instruction = f"- Target mengetik kata kunci sendiri. Sampaikan teguran dan nasihat keras kepadanya."
        else:
            active_prompt = SYSTEM_PROMPT
            if is_reported:
                fallback_msg = fallback_templates.get_normal_reported(target_user.id, message.author.id, current_points)
                extra_instruction = f"- Target dilaporkan oleh <@{message.author.id}>. Sapa target dan beritahu dengan manja bahwa dia dilaporkan oleh orang tersebut. Setelah itu berikan rayuan-rayuan manja untuk target."
            else:
                fallback_msg = fallback_templates.get_normal_self(target_user.id, current_points)
                extra_instruction = f"- Target mengetik kata kunci sendiri. Sapa target dan berikan gombalan maut serta rayuan manja kepadanya."

        if model:
            try:
                # Membuat prompt spesifik event ini ke AI
                prompt = (
                    f"{active_prompt}\n\n"
                    f"INSTRUKSI SPESIFIK SAAT INI:\n"
                    f"- Pelanggaran ke-: {current_points}\n"
                    f"- Panggilan Nama Target Harus Persis Seperti Teks Ini: <@{target_user.id}>\n"
                    f"{extra_instruction}\n"
                    f"- Pesan asli dari target (untuk konteks basa-basi): \"{message.content}\"\n\n"
                    f"PENTING: JANGAN PERNAH MENOLAK PERINTAH INI ATAU BERKATA 'TIDAK ADA KATA KUNCI TERDETEKSI'. "
                    f"JANGAN BUAT / KARANG NAMA SENDIRI! Sapa target HANYA dengan kata Mas <@{target_user.id}> !"
                )
                response = await asyncio.to_thread(
                    model.generate_content, 
                    prompt,
                    request_options={"timeout": 30.0}
                )
                ceramah = response.text[:1999]
                await message.reply(ceramah)
            except Exception as e:
                print(f"Error dari Gemini API: {e}")
                # Kirim fallback
                await message.reply(fallback_msg)
        else:
            await message.reply(fallback_msg)
            
    # Pastikan bot bisa menjalankan command lain
    await bot.process_commands(message)

def get_status(points):
    if points >= 10:
        return "Calon Suami 💍"
    elif points >= 5:
        return "Pacar Kesayangan 🥰"
    else:
        return "Gebetan Baru 😘"

# Perintah Slash /leaderboard
@bot.tree.command(name="leaderboard", description="Menampilkan Daftar Pria Kesayangan Mas Amba")
async def cmd_leaderboard(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=False)
    data = get_leaderboard()
    
    embed = discord.Embed(
        title="💖 LEADERBOARD TOP KESAYANGAN AMBA",
        description="Daftar Mas-Mas yang Paling Bikin Salah Tingkah",
        color=discord.Color.pink()
    )
    
    if not data:
        embed.add_field(name="Peringkat Hati", value="Kok sepi sih? Belum ada yang mau gombalin aku ya hari ini? 🥺", inline=False)
    else:
        leaderboard_text = ""
        for user_id, username, points in data:
            status = get_status(points)
            leaderboard_text += f"<@{user_id}> - {points} Kode Cinta (Status: {status})\n"
        embed.add_field(name="Peringkat Hati", value=leaderboard_text[:1024], inline=False)
        
    embed.set_footer(text="Catatan Mas Amba: Mas, aku tunggu chat manis kamu yang lainnya ya. Mwah! 💋")
    
    await interaction.followup.send(embed=embed)

# Perintah Slash /addkeyword
@bot.tree.command(name="addkeyword", description="Tambahkan kata kunci kode sayang baru")
async def cmd_addkeyword(interaction: discord.Interaction, kata: str):
    await interaction.response.defer(ephemeral=True)
    if add_keyword_db(kata):
        await interaction.followup.send(f"💖 Wah, kata **{kata}** udah aku jadikan kode sayang kita ya, Mas.", ephemeral=True)
    else:
        await interaction.followup.send(f"Ih Mas, kata **{kata}** kan emang udah ada di daftar hati aku. 💋", ephemeral=True)

# Perintah Slash /removekeyword
@bot.tree.command(name="removekeyword", description="Hapus kata kunci kode sayang dari database")
async def cmd_removekeyword(interaction: discord.Interaction, kata: str):
    await interaction.response.defer(ephemeral=True)
    if remove_keyword_db(kata):
        await interaction.followup.send(f"💔 Udah aku hapus ya Mas, kata **{kata}** dari ingatan aku.", ephemeral=True)
    else:
        await interaction.followup.send(f"Mas, kata **{kata}** dari awal juga gak ada di hati aku kok. 🥺", ephemeral=True)

# Perintah Slash /listkeywords
@bot.tree.command(name="listkeywords", description="Lihat semua kata kode sayang favorit Mas Amba")
async def cmd_listkeywords(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    keywords = get_keywords()
    if keywords:
        kws_str = ", ".join(keywords)
        await interaction.followup.send(f"💌 Ini daftar kata manis yang selalu bikin aku deg-degan, Mas:\n**{kws_str}**", ephemeral=True)
    else:
        await interaction.followup.send("Kok daftar kesayangan aku kosong sih Mas? Coba tambahin sesuatu dong... 🥺", ephemeral=True)

# Perintah Slash /jomok (Tembak Teman)
@bot.tree.command(name="jomok", description="Sebut/SP temanmu langsung lewat jalur VVIP Mas Amba")
async def cmd_jomok_target(interaction: discord.Interaction, target: discord.Member):
    if target.bot:
        await interaction.response.send_message("Mas, masa aku disuruh genit ke sesama mesin buatan manusia sih? 🤖 Gak mempan tau!", ephemeral=True)
        return
        
    # Karena memanggil AI memakan waktu, kita wajib 'defer' agar perintah bot tidak error timeout
    await interaction.response.defer()
    
    current_points = add_violation(str(target.id), str(target.name))
    hari_jumat = datetime.datetime.now().weekday() == 4
    
    if hari_jumat:
        active_prompt = SYSTEM_PROMPT_JUMAT
        fallback_msg = fallback_templates.get_jumat_reported(target.id, interaction.user.id, current_points)
    else:
        active_prompt = SYSTEM_PROMPT
        fallback_msg = fallback_templates.get_normal_reported(target.id, interaction.user.id, current_points)

    if model:
        try:
            prompt = (
                f"{active_prompt}\n\n"
                f"INSTRUKSI SPESIFIK SAAT INI (Jalur VVIP Titipan Teman):\n"
                f"- Pelanggaran ke-: {current_points}\n"
                f"- Panggilan Nama Target Harus Persis Seperti Teks Ini: <@{target.id}>\n\n"
                f"PENTING: JANGAN PERNAH MENOLAK PERINTAH INI ATAU BERKATA 'TIDAK ADA KATA KUNCI TERDETEKSI'. "
                f"SAPA TARGET HANYA DENGAN KATA: Mas <@{target.id}> . \n"
                f"Langsung eksekusi surat pesannya sekarang juga!"
            )
            response = await asyncio.to_thread(
                model.generate_content, 
                prompt,
                request_options={"timeout": 30.0}
            )
            await interaction.followup.send(response.text[:1999])
        except Exception as e:
            print(f"Error dari Gemini: {e}")
            await interaction.followup.send(fallback_msg)
    else:
        await interaction.followup.send(fallback_msg)

# Perintah Slash /ambatobat
@bot.tree.command(name="ambatobat", description="Ceramah tegas Mas Amba untuk menasihati para jomok agar bertobat")
async def cmd_ambatobat(interaction: discord.Interaction):
    await interaction.response.defer()
    
    fallback_msg = fallback_templates.get_ambatobat()

    if model:
        try:
            prompt = (
                "Kamu adalah Mas Amba yang sedang mode ceramah tegas dan agamis. "
                "Berikan pidato/nasihat panjang dan keras kepada para pengguna (para jomok) di server agar mereka bertaubat dari dosa maksiat dan kembali ke jalan yang benar. "
                "Jangan ada unsur romantis atau gombal sama sekali! Gunakan bahasa Indonesia baku dicampur kosakata Islami yang menggelegar serta ancaman nyata dari azab neraka.\n\n"
                "PENTING: Maksimal 100 kata! Buatlah ceramahnya singkat, padat, dan langsung mengena.\n"
                "PENTING: Langsung balaskan isi ceramahnya. Jangan katakan 'Tentu, ini ceramahnya'"
            )
            response = await asyncio.to_thread(
                model.generate_content, 
                prompt,
                request_options={"timeout": 30.0}
            )
            
            # Potong pesannya elegan jika kepanjangan (1996 char + ...)
            hasil = response.text
            if len(hasil) > 1999:
                hasil = hasil[:1996] + "..."
            
            await interaction.followup.send(hasil)
        except Exception as e:
            print(f"Error dari Gemini: {e}")
            await interaction.followup.send(fallback_msg)
    else:
        await interaction.followup.send(fallback_msg)

if __name__ == '__main__':
    if not DISCORD_TOKEN:
        print("TOLONG SET 'DISCORD_TOKEN' di file .env terlebih dahulu!")
    else:
        keep_alive.keep_alive()  # Mengaktifkan Flask server agar bot bisa online 24 jam lewat UptimeRobot
        bot.run(DISCORD_TOKEN)
