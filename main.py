import telebot
import time
import threading
import requests
from io import BytesIO

# Token bot dari @BotFather
TOKEN = "8763413992:AAGHLdEkzr1d4F-JokJuuojP4B1SDwKTu7U"
bot = telebot.TeleBot(TOKEN)

# ID grup (isi dengan ID grup Anda, bisa kosongkan dulu)
GROUP_ID = -1001234567890  # Ganti dengan ID grup Anda (negatif untuk grup)

# URL foto dari GitHub
FOTO_URL = "https://raw.githubusercontent.com/DGXEONHOZOOMD/JUALAKUNTIKTOK2026/main/Screenshot_20260327-084013.png"

# Pesan promosi yang akan dikirim berulang
PROMO_MESSAGE = """🔥 *JUAL AKUN TIKTOK SIAP PAKAI* 🔥

✅ Aman & Amanah
✅ Tidak ada pelanggaran / bersih
✅ Siap FYP (cocok untuk konten jualan)
✅ Bisa Affiliate (cairkan cuan 💰)
✅ Sudah bisa LIVE
✅ Cocok untuk bisnis / personal branding

💸 *Harga: 250K saja*

📲 *Minat langsung hubungi:*
WhatsApp: 628999859595
Telegram: t.me/DGXEONHOZOOMDBYPASS

⚡ Fast respon
⚡ Siap pakai langsung tanpa ribet
"""

# Variabel untuk post otomatis
auto_post_active = True
post_interval = 30  # 30 detik
last_post_time = 0

# Fungsi untuk download foto
def get_photo_bytes():
    try:
        response = requests.get(FOTO_URL, timeout=10)
        if response.status_code == 200:
            return BytesIO(response.content)
        return None
    except Exception as e:
        print(f"Error downloading photo: {e}")
        return None

# Fungsi untuk mengirim pesan ke grup
def send_to_group():
    try:
        photo_bytes = get_photo_bytes()
        if photo_bytes:
            bot.send_photo(
                GROUP_ID,
                photo_bytes,
                caption=PROMO_MESSAGE,
                parse_mode="Markdown"
            )
        else:
            bot.send_message(
                GROUP_ID,
                PROMO_MESSAGE,
                parse_mode="Markdown"
            )
        print(f"✅ Pesan terkirim ke grup {GROUP_ID}")
        return True
    except Exception as e:
        print(f"❌ Gagal kirim ke grup: {e}")
        return False

# Thread untuk post otomatis
def auto_post_loop():
    global auto_post_active, last_post_time
    while True:
        if auto_post_active:
            current_time = time.time()
            if current_time - last_post_time >= post_interval:
                send_to_group()
                last_post_time = current_time
        time.sleep(5)  # Cek setiap 5 detik

# Handler untuk pesan masuk (menanggapi chat)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Balas otomatis jika ada yang chat
    if message.text:
        response = f"""🔥 *HARGA AKUN TIKTOK 250K* 🔥

✅ Aman & Amanah
✅ Bisa LIVE & Affiliate
✅ Siap FYP

📲 *Order langsung:*
WhatsApp: 628999859595
Telegram: t.me/DGXEONHOZOOMDBYPASS

⚡ Fast respon!"""
        
        bot.reply_to(
            message,
            response,
            parse_mode="Markdown"
        )
        print(f"💬 Membalas pesan dari {message.from_user.first_name}: {message.text[:50]}")

# Handler untuk member join grup
@bot.message_handler(content_types=['new_chat_members'])
def handle_new_member(message):
    for new_member in message.new_chat_members:
        welcome_msg = f"""🔥 *WELCOME TO GROUP* 🔥

{new_member.first_name}, siap dapetin akun TikTok premium?

✅ Aman & Amanah
✅ Bisa LIVE & Affiliate
✅ Harga 250K saja

📲 *Order:*
WhatsApp: 628999859595
Telegram: t.me/DGXEONHOZOOMDBYPASS"""
        
        bot.send_message(
            message.chat.id,
            welcome_msg,
            parse_mode="Markdown"
        )
        print(f"👤 Member baru join: {new_member.first_name}")

# Jalankan thread auto post
def start_auto_post():
    thread = threading.Thread(target=auto_post_loop)
    thread.daemon = True
    thread.start()
    print("🚀 Auto post thread dimulai")

# Main program
if __name__ == "__main__":
    print("=" * 60)
    print("🤖 BOT PENJUALAN AKUN TIKTOK - MODE GRUP")
    print("=" * 60)
    print(f"✅ Bot berjalan dengan token: {TOKEN[:10]}...")
    print(f"📱 Group ID: {GROUP_ID}")
    print(f"🖼️ Foto dari: {FOTO_URL}")
    print(f"⏱️ Interval: {post_interval} detik")
    print(f"🔄 Auto post: {'AKTIF' if auto_post_active else 'NONAKTIF'}")
    print("=" * 60)
    print("📌 FITUR:")
    print("  • Auto post ke grup setiap 30 detik")
    print("  • Balas otomatis ke semua pesan")
    print("  • Welcome message untuk member baru")
    print("=" * 60)
    print("Bot sedang berjalan...")
    print("Tekan Ctrl+C untuk menghentikan")
    print("=" * 60)
    
    # Start auto post thread
    start_auto_post()
    
    # Start bot
    try:
        bot.infinity_polling(timeout=60)
    except Exception as e:
        print(f"❌ Error: {e}")
