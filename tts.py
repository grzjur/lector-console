from config import config
import edge_tts

async def text_to_speech_async(text):
    try:
        communicate = edge_tts.Communicate(text)
        await communicate.save(config.OUTPUT_AUDIO)
    except Exception as e:
        print(f"Error: {e}")