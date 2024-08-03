import os
import subprocess

from transliterate import translit

##Для conq
from TTS.api import TTS
import torch

import config

class VoiceAssistant:
    def __init__(self, name):
        self.name = name
        self.language =config.language
        self.engine = 'conq'
        self.translit: bool = False

        if self.engine == 'conq':
            self.sample_wave='samples/sagara_full_1.mp3'       #путь к файлу с образцом голоса
            self.conq_device = "cuda" if torch.cuda.is_available() else "cpu"
            self.conq_tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(self.conq_device)


    def say(self, text):
       
        if (self.engine == 'conq'):
            if self.translit:
                text =translit(text, self.language)
            self.conq_tts.tts_to_file(text=text, 
                                      speaker_wav=self.sample_wave, 
                                      language=self.language, 
                                      file_path="output/multi_speaker_output.wav"
                                      )
            with open(os.devnull, 'w') as devnull:
                subprocess.call(['mplayer', 'output/multi_speaker_output.wav'], stdout=devnull, stderr=devnull)

vass = VoiceAssistant("Сагара")

if __name__ == '__main__':

    pass
