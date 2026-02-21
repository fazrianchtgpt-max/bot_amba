# 💖 Bot Discord Mas Amba - Sang Pria Romantis (dan Penceramah Tegas!)

Bot Discord interaktif dua kepribadian berbasis AI (Google Gemini) yang siap meramaikan server Anda! 

Di hari biasa, **Mas Amba** adalah sosok pria manja yang merespons "kata-kata khusus" (kode sayang/jomok) dari anggota grup dengan gombalan maut dan rayuan genit yang di-generate langsung oleh AI. Namun, ketika hari berganti menjadi **Jumat**, Mas Amba berubah drastis menjadi sosok penceramah agamis yang tegas dan menggelegar, siap meruqyah dan menasihati para ahli maksiat di server Anda agar segera bertaubat!

## ✨ Fitur Utama Tersedia

- **💌 Pengawas Pesan Dinamis (AI Generated)**
  Mas Amba mengintai obrolan grup dengan seksama. Jika ia mendeteksi kata kunci pelatuk (seperti *jomok, ngawi, amba*, dll.), ia akan langsung membalas pengirimnya. Balasan ini bukan _template_ kaku, melainkan teks unik yang dirangkai langsung oleh kepintaran buatan Google Gemini.
- **🕌 Mode Suci: Jumat Tobat**
  Sistem tanggal otomatis! Setiap hari Jumat, semua unsur genit lenyap. Mas Amba akan memberikan **Surat Peringatan Jumat** berisi ceramah panjang, keras, dan ancaman nyata dari azab neraka bagi siapapun yang berani mengetik kata-kata terlarang di hari suci tersebut.
- **� Deteksi Tag Teman (Fitur Lapor VVIP)**
  Jika seorang user mengetik kata kunci sambil men-tag (mention) orang lain, Mas Amba cukup cerdas untuk mengetahui bahwa itu adalah "Laporan". Mas Amba akan menyerang (menggombal/menceramahi) target yang di-tag, sambil menyebutkan siapa nama pelapornya.
- **🏆 Papan Peringkat Hati (Leaderboard)**
  Setiap pelanggaran/kode sayang yang diketik akan menambah 1 poin. Peringkat ini diurutkan dan diberi status spesial:
  - 1-4 Poin : **Gebetan Baru 😘**
  - 5-9 Poin : **Pacar Kesayangan 🥰**
  - 10+ Poin : **Calon Suami 💍**
  *(Papan peringkat ini akan otomatis di-reset dari nol setiap 7 hari sekali untuk menjaga persaingan tetap seru!)*
- **🛡️ Sistem Tahan Banting Limit AI (Fallback Anti-Galau)**
  Jika terjadi kendala server Google API, kehabisan limit gratis, atau koneksi yang melambat (lewat 30 detik), bot tidak akan _crash/error_! Mas Amba secara otomatis akan menggunakan puluhan **Template Fallback Random** yang tak kalah lucu agar bot kalian tidak pernah bisu.

## 🤖 Perintah Interaktif (Slash Commands /)

Semua interaksi utilitas bot dapat diakses menggunakan perintah bawaan Discord (/).

- `/ambatobat` - Perintah instan untuk menurunkan pedato/ceramah keras dadakan kepada warganya tanpa harus menunggu ada yang melanggar. Cocok untuk meruqyah server yang sedang kacau!
- `/leaderboard` - Menampilkan klasemen pria-pria atau target yang paling sering mengumpulkan dosa/poin sayang di database Mas Amba.
- `/jomok @target` - Perintah tembak langsung! Menyerang teman yang di-tag melalui jalur khusus tanpa memicu pelanggaran di nama Anda sendiri.
- `/listkeywords` - Melihat seluruh ucapan sakti (daftar *keyword*) yang membuat Mas Amba terpancing.
- `/addkeyword <kata>` - (Admin/Staff) Menambahkan kata sandi baru ke dalam sistem pengawasan Mas Amba.
- `/removekeyword <kata>` - (Admin/Staff) Menghapus kata sandi dari pengawasan.

## ⚙️ Persiapan dan Instalasi

Jika Anda ingin menjalankan atau memodifikasi bot ini secara mandiri:

1. **Pastikan Python Beroperasi**
   Pastikan sistem operasi Anda sudah terinstal **Python versi 3.8 ke atas**.

2. **Instalasi Pustaka (Libraries)**
   Buka terminal di lokasi *folder* bot dan ketikkan perintah:
   ```bash
   pip install -r requirements.txt
   ```

3. **Konfigurasi Kunci (API Keys)**
   Ubah file `.env.example` menjadi `.env` saja. Kemudian buka dan isi kunci rahasianya:
   - `DISCORD_TOKEN`: Token rahasia bot dari [Discord Developer Portal](https://discord.com/developers).
   - `GEMINI_API_KEY`: Kunci API Google Gemini (AI Studio) milik Anda.

## 🚀 Cara Menghidupkan Bot

Jalankan perintah ini di dalam direktori proyek:
```bash
python main.py
```

Jika terminal menampilkan pesan `[INFO] discord.gateway: Shard ID None has connected to Gateway`, artinya Mas Amba telah bangun dan siap meramaikan (sekaligus menceramahi) server Discord Anda! 

Jangan lupa untuk mengundang (Invite Bot) melalui menu OAuth2 > URL Generator di Discord Developer dengan minimal mencentang tipe masuk `bot` serta `applications.commands`.
