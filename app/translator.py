from openai import OpenAI

from app.config import (
    OPENAI_API_KEY,
    MODEL_NAME
)

from app.prompts import SYSTEM_PROMPT
from app.dictionary import dictionary_to_prompt

client = OpenAI(
    api_key=OPENAI_API_KEY
)


def translate(text: str) -> str:
    """
    Dịch Việt ⇄ Trung
    """

    system_prompt = (
        SYSTEM_PROMPT
        + "\n\n"
        + "========================\n"
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
                    "content": text
                }
            ]
        )

        answer = response.choices[0].message.content

        if answer:
            return answer.strip()

        return "Không có kết quả."

    except Exception as e:

        print(e)

        return "❌ AI đang bận, vui lòng thử lại."
