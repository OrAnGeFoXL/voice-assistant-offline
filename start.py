import speech_recognition as sr
#import pyaudio
import os
import random

#import subprocess
#import pyttsx3
#from gtts import gTTS
from routing import start_routing

from assist import vass

#import time

import config

def active_listening(source, r):
        while True:
            phrases = ["Говорите", "Слушаю", "Eщё", "В твоём распоряжении", "Продолжим"]
            vass.say(random.choice(phrases))

            r.adjust_for_ambient_noise(source=source, duration=0.5)
            audio = r.listen(source, timeout=10, phrase_time_limit=None)

            # Сохранение аудио в файл
            with open("output/active_audio.wav", "wb") as f:
                f.write(audio.get_wav_data())          

            # Попытка распознать сказанное
            try:
                text = r.recognize_google(audio, language=config.recognize_language)

                print("Текст: " + text)
                if config.bye_phrase.lower() in text.lower():
                    vass.say('Пока, хозяин')
                    break

                start_routing(text)

            except sr.UnknownValueError:
                vass.say("Я не понимаю тебя")
            except sr.WaitTimeoutError:
                print("\033[91mПревышено время ожидания\033[0m")
                break
            except sr.RequestError as e:
                print("Неудалось запросить результаты от сервиса распознавания речи; {0}".format(e))

def passive_listening(source, r):
    
    while True:
        print("Пассивный режим прослушивания эфира")
        audio = r.listen(source, timeout=10, phrase_time_limit=None)
        with open("output/passive_audio.wav", "wb") as f:
            f.write(audio.get_wav_data())
        
        try:
            text = r.recognize_google(audio, language=config.recognize_language)

            if vass.name.lower() in text.lower():
                vass.say('Привет, хозяин')               
                active_listening(source, r)

            else:
                print(f'{text} не содержит активационное слово {vass.name}')
                      
        except sr.RequestError as e:
            print("Неудалось запросить результаты от сервиса распознавания речи; {0}".format(e))
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
        except sr.WaitTimeoutError:
            print("\033[91mПревышено время ожидания\033[0m")


def main():
    r = sr.Recognizer()
    # Получение списка устройств
    #devices = sr.Microphone.list_microphone_names()
    # Вывод списка устройств
    #for i, device in enumerate(devices):
        #print(f"{i}: {device}")

    # Использование микрофона в качестве источника звука
    with sr.Microphone(
        device_index=config.device_index,
        sample_rate=config.sample_rate,
        chunk_size=config.chunk_size
        ) as source:
        
        passive_listening(source, r)

if __name__ == "__main__":
    main()