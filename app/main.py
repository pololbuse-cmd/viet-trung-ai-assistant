import logging

from telegram import Update
from telegram.ext import (
    Application,
    MessageHandler,
    CommandHandler,
    ContextTypes,
    filters
)

from app.config import TELEGRAM_TOKEN
from app.commands import (
    start,
    help_command,
    turn_on,
    turn_off,
    group_status
)

from app.translator import translate
from app.voice import speech_to_text
from app.filters import should_translate
from app.utils import (
    clean_text,
    limit_text,
    log_error
)


# ==========================
# Logging
# ==========================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


logger = logging.getLogger(__name__)


# ==========================
# Xử lý tin nhắn
# ==========================

async def translate_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    try:

        # Không có message
        if not update.message:
            return


        # Không xử lý message không có text
        text = update.message.text

        if not text:
            return


        # Không tự dịch tin nhắn của bot
        if update.message.from_user:

            if update.message.from_user.is_bot:
                return


        # Làm sạch nội dung
        text = clean_text(text)


        # Kiểm tra có cần dịch không
        if not should_translate(text):
            return


        # Kiểm tra trạng thái nhóm

        chat_id = str(
            update.effective_chat.id
        )


        # Nếu nhóm chưa có cấu hình
        # mặc định bật

        if chat_id not in group_status:

            group_status[chat_id] = True


        # Nếu nhóm đã tắt

        if not group_status[chat_id]:
            return


        # Gọi AI dịch

        answer = translate(text)


        if not answer:
            return


        # Giới hạn độ dài Telegram

        answer = limit_text(answer)


        await update.message.reply_text(
            answer,
            reply_to_message_id=
            update.message.message_id
        )


    except Exception as e:

        log_error(e)

# ==========================
# Xử lý lỗi toàn hệ thống
# ==========================

async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE
):

    try:

        logger.error(
            "Exception while handling update:",
            exc_info=context.error
        )

        log_error(
            context.error
        )

    except Exception as e:

        log_error(e)



# ==========================
# Khởi tạo Telegram Bot
# ==========================

def create_application():

    app = (
        Application
        .builder()
        .token(
            TELEGRAM_TOKEN
        )
        .build()
    )


    # ======================
    # Commands
    # ======================

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    app.add_handler(
        CommandHandler(
            "help",
            help_command
        )
    )


    app.add_handler(
        CommandHandler(
            "on",
            turn_on
        )
    )


    app.add_handler(
        CommandHandler(
            "off",
            turn_off
        )
    )



    # ======================
    # Tin nhắn thường
    # ======================

    app.add_handler(
        MessageHandler(
            filters.TEXT
            & ~filters.COMMAND,
            translate_message
        )
    )


    # ======================
    # Error handler
    # ======================

    app.add_error_handler(
        error_handler
    )


    return app

# ==========================
# Chạy Bot
# ==========================

def main():

    try:

        app = create_application()

        print(
            "🤖 AI Translator Pro Bot running..."
        )

        logger.info(
            "Bot started successfully"
        )


        app.run_polling()


    except Exception as e:

        log_error(e)



# ==========================
# Entry Point
# ==========================

if __name__ == "__main__":

    main()

