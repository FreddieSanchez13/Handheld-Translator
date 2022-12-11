from googletrans import Translator, constants
from pprint import pprint
from recognition import recognize_speech_from_mic
from textToSpeech import speak
import speech_recognition as sr
import pocketsphinx
import time

rawAudio = sr.Recognizer()
mic = sr.Microphone()

translator = Translator()
fullLang = ""
while True:
    #tOrF = input("Would you like your sentence to be translated (to) or (from) English? (or type exit to exit)\n--> ")
    tOrF = input("Would you like your sentence to be translated (from) English? (or type exit to exit)\n--> ")
    tOrF.lower()

    #if tOrF == "to":
    #    lang = input("What language would you like translated to English?\nEspañol(es)\nDeutsch(de)\n中国人(zh)\nعربى(ar)\nfrançais(fr)\n--> ")
    #    sent = input("What sentence would you like translated?\n--> ")
        #print("(Speak your sentence to be translated)")

    #    translation = translator.translate(sent, src = lang)
    #    print("")
    #    print(f"\"{translation.origin}\" is \"{translation.text}\" in English.\n")

    if tOrF == "from":
        print("")
        lang2 = input("What language would you want your sentence to be translated to?\nEspañol(es)\nDeutsch(de)\n中国人(zh)\nعربى(ar)\nFrançais(fr)\n--> ")
        
        PROMPT_LIMIT = 5
        for j in range(PROMPT_LIMIT):
            print("")
            print("What sentence would you like translated?\n")
            text = recognize_speech_from_mic(rawAudio, mic)
            if text["transcription"]:
                break
            if not text["success"]:
                break
            print("I didn't catch that. What did you say?\n")
        if text["error"]:
            print("ERROR: {}".format(text["error"]))
            break
        print("The sentence you want translated is: {}".format(text["transcription"]))

        sent2 = text["transcription"]
        if lang2 == "es":
            fullLang = "Español"
        if lang2 == "de":
            fullLang = "Deutsch"
        if lang2 == "zh":
            fullLang = "中国人"
        if lang2 == "ar":
            fullLang = "عربى"
        if lang2 == "fr":
            fullLang = "Français"
        translation = translator.translate(sent2, dest=lang2)
        print("")
        print(f"\"{translation.origin}\" is \"{translation.text}\" in {fullLang}.\n")
        translated = translation.text
        speak(translated, lang2)

    if tOrF == "exit":
        break
    

print("")
print("Goodbye\n")

