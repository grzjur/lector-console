from litellm import acompletion
from config import config

async def generate_response(chat_history):
    try:
        response = await acompletion(
            model= config.MODEL,
            messages=chat_history
        )
        response_text = response["choices"][0]["message"]["content"]
        return response_text
    except Exception as e:
        print(f"Error: {e}")
