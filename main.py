from pyrogram import Client, idle
from config import api_id, api_hash, bot_token
from handlers.general import app as general_handler

app = Client("telegram_bot", api_id, api_hash, bot_token=bot_token)

if __name__ == "__main__":
    general_handler.start()
    app.run()
    idle()
