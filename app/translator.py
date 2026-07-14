from openai import OpenAI

from app.config import (
    OPENAI_API_KEY,
    MODEL_NAME
)

from app.prompts import SYSTEM_PROMPT
from app.dictionary import dictionary_to_prompt
from app.language import detect_language


client = OpenAI(
    api_key=OPENAI_API_KEY
)


def translate(text: str) -> str:
    """
    Dịch Việt ⇄ Trung
    """

    if not text:
        return ""

    text = text.strip()

    if len(text) > 3000:
        text = text[:3000]

    lang = detect_language(text)

    if lang == "zh":
        direction = "Hãy dịch toàn bộ nội dung sau từ TIẾNG TRUNG sang TIẾNG VIỆT. Không giữ nguyên tiếng Trung."
    elif lang == "vi":
        direction = "Hãy dịch toàn bộ nội dung sau từ TIẾNG VIỆT sang TIẾNG TRUNG GIẢN THỂ."
    else:
        direction = (
            "Hãy tự xác định ngôn ngữ. "
            "Nếu là tiếng Trung thì dịch sang tiếng Việt. "
            "Nếu là tiếng Việt thì dịch sang tiếng Trung."
        )

    system_prompt = (
        SYSTEM_PROMPT
        + "\n\n========================\n"
        + "THUẬT NGỮ BẮT BUỘC\n"
        + "========================\n"
        + dictionary_to_prompt()
    )

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": direction + "\n\n" + text
                }
            ]
        )

        answer = response.choices[0].message.content

        if answer:
            return answer.strip()

        return ""

    except Exception as e:
        print("OpenAI Error:", e)
        return "❌ AI đang bận, vui lòng thử lại."
