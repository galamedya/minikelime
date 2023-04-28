from pyrogram import Client, filters
from utils.language import translate

general_handler = Client("telegram_bot")

@general_handler.on_message(filters.command(["start"]))
def start(client, message):
    response = translate("start")
    message.reply_text(response)
