import asyncio
import os
from telegram.ext import ApplicationBuilder, CommandHandler
from fonts import fonts_data

BOT_TOKEN = os.getenv('8837685584:AAExZCf_QFxvOfHp-12qBa17J9XktGmcRqI')
async def start(update, context):
    await update.message.reply_text("Bot chal gaya 🔥\n/font naam bhej")

async def font(update, context):
    # tera font wala logic yaha
    pass

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("font", font))
    print("Bot started...")
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
