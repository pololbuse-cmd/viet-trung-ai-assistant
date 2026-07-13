import re


def is_chinese(text: str) -> bool:
    """
    Kiểm tra có chứa tiếng Trung hay không.
    """

    return bool(
        re.search(
            r'[\u4e00-\u9fff]',
            text
        )
    )


def is_vietnamese(text: str) -> bool:
    """
    Kiểm tra có chứa ký tự tiếng Việt.
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


def detect_language(text: str) -> str:
    """
    Trả về:
        zh : Tiếng Trung
        vi : Tiếng Việt
        unknown : Không xác định
    """

    if is_chinese(text):
        return "zh"

    if is_vietnamese(text):
        return "vi"

    return "unknown"
