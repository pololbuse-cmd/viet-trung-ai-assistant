from telegram.ext import (
    Application,
    CommandHandler
)

from app.config import TELEGRAM_TOKEN


async def start(update, context):

    await update.message.reply_text(
        "🤖 VietTrung AI Assistant đã hoạt động."
    )


def main():

    app = Application.builder()\
        .token(TELEGRAM_TOKEN)\
        .build()


    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    print(
        "VietTrung AI Assistant running..."
    )


    app.run_polling()


if __name__ == "__main__":
    main()
