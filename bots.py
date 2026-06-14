from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from fonts import *

TOKEN = "8837685584:AAExZCf_QFxvOfHp-12qBa17J9XktGmcRqI"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome To Yash Bots\n\n"
        "Send any text and get stylish fonts."
    )


async def convert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    result = []

    # Real Fonts
    result.append("𝗕𝗼𝗹𝗱\n" + text.translate(BOLD))
    result.append("𝘐𝘵𝘢𝘭𝘪𝘤\n" + text.translate(ITALIC))
    result.append("𝘽𝙤𝙡𝙙 𝙄𝙩𝙖𝙡𝙞𝙘\n" + text.translate(BOLD_ITALIC))
    result.append("𝙈𝙤𝙣𝙤𝙨𝙥𝙖𝙘𝙚\n" + text.translate(MONO))
    result.append("𝔻𝕠𝕦𝕓𝕝𝕖 𝕊𝕥𝕣𝕦𝕔𝕜\n" + text.translate(DOUBLE))

    # Custom Styles
    result.append("Small Caps\n" + small_caps(text))
    result.append(boxed(text))
    result.append(fancy(text))
    result.append(crown(text))
    result.append(fire(text))

    await update.message.reply_text("\n\n".join(result))


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            convert
        )
    )

    print("Yash Bots Running...")
    app.run_polling()


if __name__ == "__main__":
    main()

