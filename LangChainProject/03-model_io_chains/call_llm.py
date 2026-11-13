from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def call_with_chatcompletion():
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_API_URL"),
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "将'你好'翻译成意大利语"}],
    )

    print(f"{response.choices[0].message.content}hhhhh")

if __name__ == "__main__":
    call_with_chatcompletion()