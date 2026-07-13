import re

# Những từ không cần dịch
IGNORE_WORDS = {
    "ok",
    "oke",
    "okay",
    "ok.",
    "ok!",
    "yes",
    "yes.",
    "no",
    "no.",
    "hi",
    "hello",
    "thanks",
    "thank you",
    "haha",
    "kkk",
    "😂",
    "🤣",
    "👍",
    "👌",
    "❤️",
    "❤",
    "🙏",
    "👏",
    "🥰",
    "😍"
}


def should_translate(text: str) -> bool:
    """
    Kiểm tra xem tin nhắn có cần gửi tới AI hay không.
    """

    if not text:
        return False

    text = text.strip()

    if len(text) == 0:
        return False

    # Tin nhắn quá ngắn
    if len(text) <= 1:
        return False

    # Emoji
    if re.fullmatch(
        r'[\U0001F300-\U0001FAFF\u2600-\u27BF\s]+',
        text
    ):
        return False

    # Chỉ có số
    if text.isdigit():
        return False

    # Link
    if text.startswith(("http://", "https://")):
        return False

    # Username Telegram
    if text.startswith("@") and " " not in text:
        return False

    # Hashtag
    if text.startswith("#"):
        return False

    # Các từ phổ biến
    if text.lower() in IGNORE_WORDS:
        return False

    return True


def is_chinese(text: str) -> bool:
    """
    Kiểm tra có chứa ký tự tiếng Trung hay không.
    """
    return bool(
        re.search(
            r'[\u4e00-\u9fff]',
            text
        )
    )


def is_vietnamese(text: str) -> bool:
    """
    Kiểm tra có ký tự tiếng Việt hay không.
    """

    vietnamese_chars = (
        "ăâđêôơư"
        "àáạảã"
        "ằắặẳẵ"
        "ầấậẩẫ"
        "èéẹẻẽ"
        "ềếệểễ"
        "ìíịỉĩ"
        "òóọỏõ"
        "ồốộổỗ"
        "ờớợởỡ"
        "ùúụủũ"
        "ừứựửữ"
        "ỳýỵỷỹ"
    )

    text = text.lower()

    return any(c in text for c in vietnamese_chars)
