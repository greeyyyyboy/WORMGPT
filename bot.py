from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import asyncio
import os

TOKEN = "7796782336:AAFLAVoJ8F1_edD1fW2-wXl4P3cbQVV8nxM"  # Ganti dengan token bot Telegram
ADMIN_ID = 7215859645  # Ganti dengan ID Telegram admin

bot = Bot(token=TOKEN)
dp = Dispatcher()

USERS_FILE = "users.txt"

async def save_user(user):
    user_data = f"{user.id} - @{user.username}\n"
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            f.write(user_data)
    else:
        with open(USERS_FILE, "r") as f:
            users = f.readlines()
        if user_data not in users:
            with open(USERS_FILE, "a") as f:
                f.write(user_data)

@dp.message()
async def start(message: Message):
    if message.text == "/start":
        await save_user(message.from_user)
        await message.answer("👋 Welcome! You are now using this bot.")
    elif message.text == "/users":
        if message.from_user.id == ADMIN_ID:
            if os.path.exists(USERS_FILE):
                with open(USERS_FILE, "r") as f:
                    users_list = f.read()
                await message.answer(f"👥 *List of users:*\n\n{users_list}", parse_mode="Markdown")
            else:
                await message.answer("⚠ No users found.")
        else:
            await message.answer("❌ You are not authorized to use this command.")

async def main():
    print("Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
