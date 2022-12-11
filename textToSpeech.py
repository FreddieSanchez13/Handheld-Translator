from gtts import gTTS
import os
import playsound

def speak(text,lang):
    tts = gTTS(text=text, lang=lang)

    filename = "abc.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)