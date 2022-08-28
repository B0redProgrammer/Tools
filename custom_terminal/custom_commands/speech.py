import gtts
from playsound import playsound

import os
import sys

def speak(text):
    Path = os.path.abspath(os.getcwd())

    audio = gtts.gTTS(text)
    audio.save('audio.mp3')
    playsound('audio.mp3')

    os.system('rm {}/audio.mp3'.format(Path))

speak(sys.argv[1])
