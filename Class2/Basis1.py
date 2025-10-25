import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")

client = OpenAI(api_key=api_key, base_url=base_url)

response = client.chat.completions.create(
    model="ernie-x1.1-preview",
    messages=[
        {"role": "system", "content": "你是一个有用的助手。"},
        {"role": "user", "content": "你好，AI！"}
    ],
    max_tokens=1000
)

print(response.choices[0].message.content)
