from pyrogram import Client, filters
from models.user import User
from models.group import Group

app = Client("telegram_bot")

@app.on_message(filters.command(["admin_ekle"]))
def add_admin(client, message):
    user_id = int(message.command[1])
    user = User.get_or_create(user_id)

    if not user.is_admin():
        user.set_admin()

    message.reply_text(f"Admin eklendi: {user_id}")
