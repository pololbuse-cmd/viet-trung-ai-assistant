import json
import os

from app.config import DICTIONARY_FILE


def load_dictionary() -> dict:
    """
    Đọc dictionary.json
    """

    if not os.path.exists(DICTIONARY_FILE):
        return {}

    try:
        with open(
            DICTIONARY_FILE,
            "r",
            encoding="utf-8"
        ) as f:
            return json.load(f)

    except Exception as e:
        print(f"Lỗi đọc dictionary: {e}")
        return {}


def save_dictionary(dictionary: dict):
    """
    Ghi dictionary.json
    """

    os.makedirs(
        os.path.dirname(DICTIONARY_FILE),
        exist_ok=True
    )

    with open(
        DICTIONARY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            dictionary,
            f,
            ensure_ascii=False,
            indent=4
        )


def dictionary_to_prompt() -> str:
    """
    Chuyển dictionary thành Prompt
    """

    dictionary = load_dictionary()

    if not dictionary:
        return ""

    lines = []

    for vi, zh in dictionary.items():
        lines.append(f"{vi} = {zh}")

    return "\n".join(lines)
