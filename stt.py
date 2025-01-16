from litellm import transcription
from config import config

def speech_to_text(file_path) -> str:
    try:
        audio_file = open(file_path, "rb")
        response = transcription(model=str(config.MODEL_SPEECH_TO_TEXT), file=audio_file, language=str(config.LANG))
        return str(response.text)
    except Exception as e:
        print(f"Error: {e}")