import json
import os

from telegram import Update
from telegram.ext import ContextTypes

from app.config import GROUP_STATUS_FILE

# ==========================
# Đọc trạng thái nhóm
# ==========================

def load_group_status():

    if not os.path.exists(GROUP_STATUS_FILE):
        return {}

    try:

        with open(
            GROUP_STATUS_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except Exception:

        return {}


# ==========================
# Lưu trạng thái nhóm
# ==========================

def save_group_status(data):

    os.makedirs(
        os.path.dirname(GROUP_STATUS_FILE),
        exist_ok=True
    )

    with open(
        GROUP_STATUS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )


group_status = load_group_status()


# ==========================
# /start
# ==========================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = (
        "🤖 AI Translator Pro\n\n"
        "Tự động dịch Việt ⇄ Trung.\n\n"
        "Lệnh:\n"
        "/on - Bật dịch\n"
        "/off - Tắt dịch\n"
        "/help - Hướng dẫn"
    )

    await update.message.reply_text(text)


# ==========================
# /help
# ==========================

async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = (
        "📖 Hướng dẫn\n\n"
        "Bot sẽ tự nhận biết:\n"
        "- Tiếng Việt → Tiếng Trung\n"
        "- Tiếng Trung → Tiếng Việt\n\n"
        "Không cần gõ lệnh dịch."
    )

    await update.message.reply_text(text)


# ==========================
# /on
# ==========================

async def turn_on(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    chat_id = str(update.effective_chat.id)

    group_status[chat_id] = True

    save_group_status(group_status)

    await update.message.reply_text(
        "✅ Đã bật dịch tự động."
    )


# ==========================
# /off
# ==========================

async def turn_off(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    chat_id = str(update.effective_chat.id)

    group_status[chat_id] = False

    save_group_status(group_status)

    await update.message.reply_text(
        "⛔ Đã tắt dịch tự động."
    )
