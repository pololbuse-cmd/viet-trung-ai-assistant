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
# Xử lý tin nhắn văn bản
# ==========================

async def translate_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    try:

        if not update.message:
            return


        text = update.message.text


        if not text:
            return



        # Không dịch tin nhắn của bot

        if update.message.from_user:

            if update.message.from_user.is_bot:
                return



        print(
            "📥 RAW TEXT:",
            repr(text)
        )



        text = clean_text(text)



        print(
            "🧹 CLEAN TEXT:",
            repr(text)
        )



        # Kiểm tra filter

        if not should_translate(text):

            print(
                "❌ BỊ FILTER BỎ QUA:",
                text
            )

            return



        chat_id = str(
            update.effective_chat.id
        )



        if chat_id not in group_status:

            group_status[chat_id] = True



        if not group_status[chat_id]:

            print(
                "⛔ Nhóm đang tắt dịch"
            )

            return



        print(
            "📩 SEND TO AI:",
            text
        )



        answer = translate(
            text
        )



        if not answer:

            print(
                "⚠️ AI trả về rỗng"
            )

            return



        answer = limit_text(
            answer
        )



        await update.message.reply_text(

            answer,

            reply_to_message_id=
            update.message.message_id

        )


        print(
            "✅ TRANSLATED:",
            answer
        )



    except Exception as e:

        log_error(e)






# ==========================
# Xử lý tin nhắn giọng nói
# ==========================

async def translate_voice(

    update: Update,

    context: ContextTypes.DEFAULT_TYPE

):

    try:


        if not update.message:

            return



        if not update.message.voice:

            return



        print(
            "🎤 Voice message received"
        )



        voice = await update.message.voice.get_file()



        file_path = "voice.ogg"



        await voice.download_to_drive(

            file_path

        )



        print(
            "🔊 Voice downloaded"
        )



        text = await speech_to_text(

            file_path

        )



        if not text:

            return



        print(
            "📝 Voice text:",
            text
        )



        answer = translate(

            text

        )



        if not answer:

            return



        await update.message.reply_text(

            answer,

            reply_to_message_id=
            update.message.message_id

        )



        print(
            "✅ Voice translated"
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




    # Commands

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





    # Tin nhắn chữ

    app.add_handler(

        MessageHandler(

            filters.TEXT
            & ~filters.COMMAND,

            translate_message

        )

    )





    # Tin nhắn voice

    app.add_handler(

        MessageHandler(

            filters.VOICE,

            translate_voice

        )

    )





    # Error Handler

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
