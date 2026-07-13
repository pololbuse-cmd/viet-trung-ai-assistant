import logging
import traceback


# ==========================
# Logger
# ==========================

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


# ==========================
# Ghi log
# ==========================

def log_info(message: str):
    logger.info(message)


def log_warning(message: str):
    logger.warning(message)


def log_error(error):
    logger.error(error)
    traceback.print_exc()


# ==========================
# Làm sạch tin nhắn
# ==========================

def clean_text(text: str) -> str:
    """
    Loại bỏ khoảng trắng thừa.
    """

    if not text:
        return ""

    return " ".join(text.strip().split())


# ==========================
# Cắt tin nhắn quá dài
# ==========================

def limit_text(text: str, max_length: int = 4000) -> str:
    """
    Telegram giới hạn khoảng 4096 ký tự.
    """

    if len(text) <= max_length:
        return text

    return text[:max_length] + "..."


# ==========================
# Kiểm tra chuỗi rỗng
# ==========================

def is_empty(text: str) -> bool:

    if text is None:
        return True

    if text.strip() == "":
        return True

    return False
