# Poe to OpenAI API Converter

This project converts Poe's API for AI chatbots into an OpenAI-compatible API format. It allows Poe subscribers to utilize their monthly quota through an API that's compatible with OpenAI's format, enabling integration with various platforms that support OpenAI's API.

## Usage

1. Set up the FastAPI server using the provided code.
2. Use the OpenAI client library to interact with the API:

```python
from openai import OpenAI
import json

API_ENDPOINT = 'your_endpoint'
API_KEY = 'API_KEY' # 从 https://poe.com/api_key 获取
MODEL_NAME = 'GPT-4o-Mini' # 按照 Poe 中的命名选择模型

client = OpenAI(base_url=API_ENDPOINT, api_key=API_KEY)

print("Testing stream completion")

completion = client.completions.create(
    model=MODEL_NAME,
    prompt="Say this is a test",
    stream=True,
)

for chunk in completion:
    print(chunk.choices[0].text or "", end="")
```

## Limitations

Does not currently support Vision or other advanced features
Requires a Poe subscription

## Credits

This project is based on the excellent work shared by user affedawe on LINUX DO. We extend our sincere thanks to affedawe for creating and sharing this valuable resource. The original post can be found at:
https://linux.do/t/topic/98971

Additional contributions and modifications by @0v0 and other community members are gratefully acknowledged.
