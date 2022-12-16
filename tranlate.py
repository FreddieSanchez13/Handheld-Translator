from googletrans import Translator, constants
from pprint import pprint
from recognition import recognize_speech_from_mic
from textToSpeech import speak
from translateToEnglish import translate_to_english
import speech_recognition as sr



rawAudio = sr.Recognizer()
mic = sr.Microphone()

translator = Translator()
fullLang = ""
while True:
    tOrF = input("Would you like your sentence to be translated (to) or (from) English? (or type exit to exit)\n--> ")
    tOrF.lower()

    if tOrF == "to":
        lang = input("What language would you like translated to English?\nEspañol(es)\nDeutsch(de)\nPortuguês(pt)\nItaliano(it)\nFrançais(fr)\n--> ")
        PROMPT_LIMIT = 5
        for j in range(PROMPT_LIMIT):
            print("")
            print("What sentence would you like translated?\n")
            sent = recognize_speech_from_mic(rawAudio, mic, lang)
            if sent["transcription"]:
                break
            if not sent["success"]:
                break
            print("I didn't catch that. What did you say?\n")
        if sent["error"]:
            print("ERROR: {}".format(sent["error"]))
            break
        print("The sentence you want translated is: {}".format(sent["transcription"]))
        translation = translate_to_english(sent, lang)

        print(f"\"{translation.origin}\" is \"{translation.text}\" in English.\n")
        translated = translation.sent
        speak(translated, lang)

    if tOrF == "from":
        print("")
        lang2 = input("What language would you want your sentence to be translated to?\nEspañol(es)\nDeutsch(de)\nPortuguês(pt)\nItaliano(it)\nFrançais(fr)\n--> ")
        
        PROMPT_LIMIT = 5
        for j in range(PROMPT_LIMIT):
            print("")
            print("What sentence would you like translated?\n")
            text = recognize_speech_from_mic(rawAudio, mic, 'en-US')
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
        if lang2 == "pt":
            fullLang = "Português"
        if lang2 == "it":
            fullLang = "Italiano"
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

