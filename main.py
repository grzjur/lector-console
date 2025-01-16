from colorama import Fore
import asyncio
from audio import record_audio_to_mp3, play_audio
from stt import speech_to_text
from tts import text_to_speech_async
from llm import generate_response
from config import config

async def main():
    try:
        chat_history = [{"role": "system", "content": config.SYSTEM_PROMPT}]
        chat_history.append({"role": "user", "content": config.USER_CONTENT_START})

        response_text = await generate_response(chat_history)
        print(Fore.MAGENTA + "  -" + response_text + Fore.RESET)
        chat_history.append({"role": "assistant", "content": response_text})
        await text_to_speech_async(response_text)
        play_audio(config.OUTPUT_AUDIO)

        while True:
            if record_audio_to_mp3(config.INPUT_AUDIO):
                user_input = speech_to_text(config.INPUT_AUDIO)
                print(Fore.GREEN +  user_input + Fore.RESET)
                if user_input.lower() == "bye" or user_input.lower() == "bye.":
                    break
                chat_history.append({"role": "user", "content": user_input})
                response_text = await generate_response(chat_history)
                print(Fore.MAGENTA + "  -" + response_text + Fore.RESET)
                chat_history.append({"role": "assistant", "content": response_text})
                await text_to_speech_async(response_text)
                play_audio(config.OUTPUT_AUDIO)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("----------------------------------------------------------------------------------------")
    print(f"\n\n\n")
    asyncio.run(main())
