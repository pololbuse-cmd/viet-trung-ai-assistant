import os
from dotenv import load_dotenv

# Đọc file .env (khi chạy trên máy)
load_dotenv()

# ===========================
# Telegram
# ===========================

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TELEGRAM_TOKEN:
    raise ValueError("Thiếu TELEGRAM_TOKEN")

# ===========================
# OpenAI
# ===========================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("Thiếu OPENAI_API_KEY")

# ===========================
# Admin
# ===========================

_admin = os.getenv("ADMIN_ID", "").strip()

if _admin.isdigit():
    ADMIN_ID = int(_admin)
else:
    ADMIN_ID = None

# ===========================
# AI Model
# ===========================

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "gpt-4.1-mini"
)

# ===========================
# Files
# ===========================

DATA_DIR = "data"

DICTIONARY_FILE = os.path.join(
    DATA_DIR,
    "dictionary.json"
)

GROUP_STATUS_FILE = os.path.join(
    DATA_DIR,
    "group_status.json"
)
