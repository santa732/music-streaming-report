import pandas as pd
import random
import requests


TELEGRAM_TOKEN = "8994630349:AAFnBQxQetHri4fxymBNevgSJGSTiMigkWc"
CHAT_ID = "1640823263" 

df = pd.read_csv("streaming_data.csv")


lagu_hari_ini = df.sample(n=1).iloc[0]

judul = lagu_hari_ini["song_title"]
penyanyi = lagu_hari_ini["artist"]
total_stream = f"{lagu_hari_ini['streams']:,}"
genre = lagu_hari_ini["genre"]


pesan_laporan = f"""
🎵 **DAILY MUSIC STREAMING REPORT** 🎵
----------------------------------
🔥 **Trending Track Today:**
• **Judul:** {judul}
• **Penyanyi:** {penyanyi}
• **Genre:** {genre}
• **Total Streams:** {total_stream} plays

📊 *Status: Data streaming otomatis diperbarui!*
"""


telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
requests.post(telegram_url, data={"chat_id": CHAT_ID, "text": pesan_laporan, "parse_mode": "Markdown"})

print("Laporan streaming data berhasil dikirim!")