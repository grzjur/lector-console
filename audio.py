from colorama import init, Fore
import pygame
import time
import sounddevice as sd
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

def record_audio_to_mp3(file_path, timeout=10, pause_threshold=2):
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = pause_threshold
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print(Fore.BLUE + "Recording..." + Fore.RESET)
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=None)
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            print(Fore.BLUE + "Recording finished" + Fore.RESET)
            return True
    except sr.WaitTimeoutError:
        print("Recording failed - timeout")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def play_audio(file_path):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        pygame.mixer.quit()
    except pygame.error as e:
        print(f"Failed to play audio: {e}")
    except Exception as e:
        print(f"Error: {e}")

