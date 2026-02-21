import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot Mas Amba sedang online (Server Web Aktif)!"

def run():
    # Render memberikan port dinamis ke variabel PORT, fallback ke 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    # Menjalankan server web Flask dalam thread terpisah agar tidak memblokir Bot Discord
    t = Thread(target=run)
    t.start()
