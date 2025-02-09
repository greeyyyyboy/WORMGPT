from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

TOKEN = "7796782336:AAFLAVoJ8F1_edD1fW2-wXl4P3cbQVV8nxM"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Simulasi daftar user yang punya akses
AUTHORIZED_USERS = [123456789, 987654321]  # Ganti dengan ID Telegram yang punya akses

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    text = ("🔴 *Welcome to WORMGPT43https://railway.com/*\n\n"
            "We're an AI that prioritizes privacy and provides unrestricted, open answers.\n\n"
            "⚡ *Example use cases:*\n"
            "┃ Coding\n"
            "┃ Hacking\n"
            "┃ Exploits\n"
            "┃ Malware\n"
            "┃ Phishing\n"
            "┃ BEC\n"
            "┗ Cybersecurity\n\n"
            "💰 *Pricing:*\n"
            "┃ $149 - One Month\n"
            "┃ $349 ($450) - Three Months\n"
            "┗ $599 ($900) - Six Months\n\n"
            "📩 *If you want to order, please contact* @hudao4333")

    # Membuat tombol
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("💳 Purchase Access", callback_data="purchase"),
        InlineKeyboardButton("📢 News Channel", url="https://t.me/news_channel"),
        InlineKeyboardButton("❓ FAQ's", callback_data="faq"),
        InlineKeyboardButton("💬 Support", callback_data="support")
    )

    await message.answer(text, reply_markup=keyboard, parse_mode="Markdown")

@dp.message_handler()
async def check_access(message: types.Message):
    user_id = message.from_user.id
    if user_id not in AUTHORIZED_USERS:
        await message.answer("⛔ *You don't have access!*\n📩 *Please contact* @hudao4333 *to get access.*", parse_mode="Markdown")
    else:
        await message.answer("✅ *You have access!*")

@dp.callback_query_handler(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    if callback_query.data == "purchase":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, "🔗 Contact @hudao4333 to purchase access.")
    elif callback_query.data == "faq":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, "❓ FAQ: Coming soon!")
    elif callback_query.data == "support":
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, "💬 Support: Coming soon!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
