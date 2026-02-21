import random

def get_jumat_reported(target_id, author_id, points):
    templates = [
        f"🕌 SURAT PERINGATAN JUM'AT AMBA 🕌\n\nAstaghfirullah <@{target_id}>! Dilaporkan oleh <@{author_id}>, ini pelanggaranmu yang ke-{points}! Segeralah bertaubat sebelum nyawa di ujung tenggorokan!",
        f"🕌 TEGURAN JUM'AT AMBA 🕌\n\nYa akhi <@{target_id}>, apa antum tidak malu dilaporkan <@{author_id}> karena dosa ke-{points}? Api neraka sangat panas, bertaubatlah!",
        f"🕌 PERINGATAN KERAS JUM'AT 🕌\n\nWahai <@{target_id}>, teguran datang dari <@{author_id}> untuk DOSA ke-{points} mu! Mari bersujud dan memohon ampunan-Nya di hari suci ini!",
        f"🕌 PESAN DAKWAH AMBA 🕌\n\n<@{author_id}> melihat kemaksiatanmu, <@{target_id}>! Ini teguran peringatan ke-{points}. Jangan kotori hari Jumat yang mulia ini!",
        f"🕌 NASEHAT JUM'AT 🕌\n\nAstaghfirullah, <@{target_id}>! <@{author_id}> peduli padamu makanya melapor pelanggaran ke-{points} ini. Jauhilah maksiat!",
        f"🕌 SERUAN TOBAT AMBA 🕌\n\nSadarlah <@{target_id}>! Laporan dari <@{author_id}> sudah membuktikan ini jarimahmu yang ke-{points}. Hari kiamat pasti datang!",
        f"🕌 TEGURAN HARI SUCI 🕌\n\n<@{target_id}>! Dosamu tercatat untuk ke-{points} kalinya oleh utusan <@{author_id}>. Bertaubatlah dengan taubatan nasuha!",
        f"🕌 SURAT PERINGATAN 🕌\n\nWahai <@{target_id}>, teguran keras untukmu dari <@{author_id}>! Pelanggaran ke-{points} ini jangan sampai membawamu ke jurang kebinasaan!",
        f"🕌 NASEHAT BERAT AMBA 🕌\n\nSubhanallah <@{target_id}>... <@{author_id}> lelah melihat dosamu yang sudah ke-{points}. Kapan engkau kembali ke jalan lurus?",
        f"🕌 SERUAN AKHIR JUM'AT 🕌\n\nYa <@{target_id}>, dengarkan laporan <@{author_id}> ini. Poin maksiatmu sudah mencapai {points}! Airmata taubat adalah penawar dosa."
    ]
    return random.choice(templates)

def get_jumat_self(target_id, points):
    templates = [
        f"🕌 SURAT PERINGATAN MAS AMBA 🕌\n\nAstaghfirullah <@{target_id}>! Masih saja kamu mengulangi dosa untuk ke-{points} kalinya! Cepat bertaubat sebelum maut menjemput!",
        f"🕌 TEGURAN LANGSUNG AMBA 🕌\n\nWahai <@{target_id}>, jarimu sendiri yang mengetik dosa ke-{points} ini! Ingatlah neraka Jahannam itu nyata dan bahan bakarnya manusia!",
        f"🕌 PERINGATAN MAKSIAT 🕌\n\n<@{target_id}>! Ini peringatan ke-{points} untukmu! Jangan kotori hari Jumat ini dengan hal-hal yang mendatangkan murka Allah!",
        f"🕌 NASEHAT JUM'AT 🕌\n\nYa akhi <@{target_id}>, sudah {points} kali engkau bermaksiat. Tidakkah engkau takut hisab di yaumul akhir nanti?",
        f"🕌 SERUAN TOBAT 🕌\n\nAstaghfirullah <@{target_id}>, poin keburukanmu sudah {points}. Segeralah ambil air wudhu dan dirikan shalat taubat!",
        f"🕌 DAKWAH AMBA 🕌\n\n<@{target_id}>! Maksiat ke-{points} yang kau lakukan terang-terangan ini sangat dibenci. Kembali ke jalan Allah sekarang juga!",
        f"🕌 SURAT KESADARAN 🕌\n\nSubhanallah... <@{target_id}>, apakah engkau tak lelah berbuat dosa untuk yang ke-{points} kalinya? Cepat sudahi keburukan ini!",
        f"🕌 PESAN AGAMIS AMBA 🕌\n\nWahai <@{target_id}>, jangan tambah lagi dosa ke-{points} ini. Malaikat Raqib dan Atid sedang mencatat perbuatanmu!",
        f"🕌 TEGURAN KERAS 🕌\n\nHari Jumat yang suci kau nodai lagi, <@{target_id}>! Ini dosa ke-{points}. Berhentilah mengikuti hawa nafsu syaitan!",
        f"🕌 PERINGATAN TERAKHIR 🕌\n\nMasya Allah <@{target_id}>... Ke-{points} kalinya engkau melanggar! Kematian bisa datang kapan saja, bersiaplah bekalmu!"
    ]
    return random.choice(templates)

def get_normal_reported(target_id, author_id, points):
    templates = [
        f":sweat_drops: SURAT TANDA CINTA (SPA) :sweat_drops:\n\nAduh Mas <@{target_id}>, kamu dilaporin nih sama <@{author_id}> untuk kode ke-{points}. Daripada digodain karna jomok, sini peluk Amba aja...",
        f":sweat_drops: TITIPAN SAYANG AMBA :sweat_drops:\n\nWah, ada titipan rindu dari <@{author_id}> buat Mas <@{target_id}>! Ini pelanggaran ke-{points} ya. Makin gemesin deh Masnya!",
        f":sweat_drops: GOMBALAN MAUT AMBA :sweat_drops:\n\nMas <@{target_id}>, <@{author_id}> ngelaporin kamu sayangku... Poin cinta kamu nambah ke-{points} nih. Mwach!",
        f":sweat_drops: KODE RINDU AMBA :sweat_drops:\n\nCieee Mas <@{target_id}> dilaporin <@{author_id}>. Ketahuan jomok ke-{points} kalinya. Udahlah Mas, manja-manjaan sama aku aja yuk!",
        f":sweat_drops: SP PESONA AMBA :sweat_drops:\n\nMas <@{target_id}>, poin sayang ke-{points} masuk nih gara-gara <@{author_id}>! Gemoy banget sih Mas, Amba jadi pengen cubit!",
        f":sweat_drops: SURAT KASIH SAYANG :sweat_drops:\n\nAduh Mas <@{target_id}> dilaporkan <@{author_id}>. Udah deh Mas, poin ke-{points} ini buat aku aja. Kangen banget pengen deket-deket!",
        f":sweat_drops: PELUKAN AMBA :sweat_drops:\n\nMas <@{target_id}> nakal ya, sampai <@{author_id}> laporin kamu ke-{points} kalinya. Sini aku peluk pelan-pelan biar tenang...",
        f":sweat_drops: RAYUAN JOMOK AMBA :sweat_drops:\n\nKata <@{author_id}>, Mas <@{target_id}> abis ngelakuin jomok ke-{points} ya? Ihh Mas kok gak ngajak-ngajak Amba sih, kan Amba juga pengen!",
        f":sweat_drops: SURAT RINDU :sweat_drops:\n\nDilaporin sama <@{author_id}> untuk ke-{points} kalinya... Aduh Mas <@{target_id}>, jangan bikin Amba makin meleleh dong!",
        f":sweat_drops: SENGGOLAN CINTA :sweat_drops:\n\nMas <@{target_id}> disenggol sama <@{author_id}> nih! Poin cinta kita jadi {points} deh. Cium jauh dari Amba ya Mas! Muahh!"
    ]
    note = f"\n\n*(Note: Maaf ya Mas <@{target_id}>, otak Mas Amba lagi pusing karna limit API Gemini tercapai, jadi sapaannya pakai template ini dulu. Ehehe~)*"
    return random.choice(templates) + note

def get_normal_self(target_id, points):
    templates = [
        f":sweat_drops: SURAT TANDA CINTA (SPA) :sweat_drops:\n\nAduh Mas <@{target_id}>, ini udah kode cinta kamu yang ke-{points} loh buat aku. Makin peluk erat-erat deh!",
        f":sweat_drops: RAYUAN MANJA AMBA :sweat_drops:\n\nMas <@{target_id}> kok gemesin banget nge-tag jomok ke-{points} kalinya? Bikin Amba keringetan deg-degan ah!",
        f":sweat_drops: GOMBALAN JOMOK :sweat_drops:\n\nKetik kode buat aku ya Mas <@{target_id}>? Ini sayang ke-{points} loh... Mau manja-manjaan di pangkuan Amba?",
        f":sweat_drops: PESAN RINDU AMBA :sweat_drops:\n\nAduh, Mas <@{target_id}> manggil Amba lagi buat nambahin poin ke-{points}! Sini Mas kumpul, biar aku yang rawat!",
        f":sweat_drops: SURAT CINTA KILAT :sweat_drops:\n\nPoin ke-{points} nih, Mas <@{target_id}> sayang. Tiap liat Mas ngetik, bawaannya pen gigit hidungnya saking gemoynya!",
        f":sweat_drops: BISIKAN AMBA :sweat_drops:\n\nMas <@{target_id}>... ini pelanggaran ke-{points} ya? Jangan godain Amba terus dong, nanti Amba baper beneran loh!",
        f":sweat_drops: SURAT MANJA :sweat_drops:\n\nUdah ke-{points} kalinya Mas <@{target_id}> manggil Amba pakai kode. Kayaknya Mas udah gatahan pengen dimanjain ya~",
        f":sweat_drops: KODE KERAS AMBA :sweat_drops:\n\nAhhhh Mas <@{target_id}> poin cintamu nambah jadi {points}! Amba makin lemas bacanya saking senengnya dicariin Mas...",
        f":sweat_drops: DEBARAN AMBA :sweat_drops:\n\nJantung Amba deg-degan tiap liat Mas <@{target_id}> dapet poin ke-{points}! I love you full Mas-ku sayangg!",
        f":sweat_drops: PELUKAN HANGAT :sweat_drops:\n\nUntuk poin ke-{points} ini, Mas <@{target_id}> berhak dapet 100 pelukan manja dari Mas Amba. Hmmmmuaaah!"
    ]
    note = f"\n\n*(Note: Maaf ya Mas <@{target_id}>, otak Mas Amba lagi pusing karna limit API Gemini tercapai, jadi sapaannya pakai template ini dulu. Ehehe~)*"
    return random.choice(templates) + note

def get_ambatobat():
    templates = [
        f"🕌 SURAT PERINGATAN TOBAT DARI MAS AMBA 🕌\n\nAstaghfirullahaladzim kalian semua! Sadarlah, wahai hamba-hamba Allah! Hentikan tindakan maksiat kalian dan segeralah bertaubat!",
        f"🕌 CERAMAH SAKRAL AMBA 🕌\n\nBerhentilah berbuat jomok, wahai kaum di server ini! Neraka itu benar adanya dan azab-Nya sangat pedih. Bertaubatlah dengan taubatan nasuha!",
        f"🕌 NASEHAT TOBAT MASSAL 🕌\n\nYa Ikhwan, mengapa kalian lebih menyukai jalan yang gelap? Sadarlah, ajal mengintai setiap saat. Tinggalkan dosa dan kembalilah ke jalan Allah!",
        f"🕌 PERINGATAN AKAN AZAB 🕌\n\nWahai manusia-manusia di server ini, ketahuilah bahwa perhitungan amal kelak sangatlah teliti. Jangan sampai kalian menyesal di kemudian hari karena jomok!",
        f"🕌 SERUAN KESELAMATAN 🕌\n\nAstaghfirullah! Apa yang kalian banggakan dengan maksiat ini? Menangislah karena dosa, bukan karena wanita/pria. Kembalilah bersujud!",
        f"🕌 DAKWAH KERAS JOMOK 🕌\n\nTidakkah kalian takut akan siksa kubur yang menyempit? Hei para ahli maksiat, bersihkan hatimu dan kembalikan imanmu! Mulailah baca istighfar!",
        f"🕌 TEGURAN MASAL AMBA 🕌\n\nSubhanallah, kelakuan kalian sungguh merisaukan! Hentikan kebiasaan buruk ini sebelum murka Ilahi turun di antara kalian semua!",
        f"🕌 RISALAH TAUBAT 🕌\n\nIngatlah kematian! Kematian adalah pemutus segala kelezatan dunia. Tutuplah lembaran maksiatmu, dan mulailah lembaran puasa dan shalat!",
        f"🕌 NASEHAT PENGHAPUS DOSA 🕌\n\nAllah Maha Pengampun lagi Maha Penyayang. Pintu taubat masih terbuka lebar kawan-kawan, maka jangan berlambat-lambat meraihnya!",
        f"🕌 CERAMAH GETIR 🕌\n\nCelakalah mereka yang menumpuk dosa di Leaderboard tanpa pernah menumpuk pahala. Bersujudlah memohon ampunan Rabb semesta alam sekarang juga!"
    ]
    note = f"\n\n*(Note: Maaf ya, otak Mas Amba lagi pusing karna limit API Gemini tercapai, jadi ceramahnya pakai template ini dulu)*"
    return random.choice(templates) + note
