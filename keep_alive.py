from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot Mas Amba sedang online (Server Web Aktif)!"

def run():
    # Gunakan port 8080 yang biasanya dipakai layanan hosting gratis (seperti Render.com)
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    # Menjalankan server web Flask dalam thread terpisah agar tidak memblokir Bot Discord
    t = Thread(target=run)
    t.start()
