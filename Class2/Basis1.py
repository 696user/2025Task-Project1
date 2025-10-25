import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")  #本地运行时，改成自己的 API Key
base_url = os.getenv("OPENAI_BASE_URL")  # 本地运行时，改成提供商给定的地址

client = OpenAI(api_key=api_key, base_url=base_url)

history = []  #对话历史记录

while True:
    prompt = input()
    if not prompt:
        break  # 输入为空时退出

    history.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="ernie-x1.1-preview",
        messages=history,
        max_tokens=1000
    )

    answer = response.choices[0].message.content
    history.append({"role": "assistant", "content": answer})
    print(answer)
