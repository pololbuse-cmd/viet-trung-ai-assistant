import os
from openai import OpenAI


client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)


async def speech_to_text(audio_file):

    with open(audio_file, "rb") as f:

        result = client.audio.transcriptions.create(
            model="whisper-1",
            file=f
        )

    return result.text
