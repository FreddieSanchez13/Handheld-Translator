import os
import tkinter as tk
import pyttsx3
import subprocess
import speech_recognition as sr

class Translator:
    def __init__(self, root):
        self.root = root
        self.root.title("Translator")

        # Set up the speech recognizer
        self.r = sr.Recognizer()
        with sr.Microphone() as source:
            # Calibrate the recognizer
            self.r.adjust_for_ambient_noise(source)

        # Set up the text-to-speech engine
        self.engine = pyttsx3.init()

        # Define the languages dictionary
        self.LANGUAGES = {
            "en": "English",
            "es": "Spanish",
            "fr": "French",
            "de": "German",
            "it": "Italian",
            "pt": "Portuguese",
        }

        # Create the dropdown menu for selecting the input language
        input_language_label = tk.Label(self.root, text="Input Language:")
        input_language_label.pack()

        self.input_language_var = tk.StringVar(self.root)
        self.input_language_var.set("en")

        input_language_menu = tk.OptionMenu(self.root, self.input_language_var, *self.LANGUAGES.keys())
        input_language_menu.pack()

        # Create the dropdown menu for selecting the output language
        output_language_label = tk.Label(self.root, text="Output Language:")
        output_language_label.pack()

        self.output_language_var = tk.StringVar(self.root)
        self.output_language_var.set("es")

        output_language_menu = tk.OptionMenu(self.root, self.output_language_var, *self.LANGUAGES.keys())
        output_language_menu.pack()

        # Create the translate button
        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate)
        self.translate_button.pack()

    def speech_recognition(self):
        # Use the speech recognizer to get the input text
        with sr.Microphone() as source:
            audio = self.r.listen(source)
        text = self.r.recognize_sphinx(audio)

        return text

    def translate(self):
        # Use speech recognition to get the input text
        text = self.speech_recognition()

        # Get the input and output languages from the dropdown menus
        input_lang = self.input_language_var.get()
        output_lang = self.output_language_var.get()

        # Use Translate-Shell to translate the text
        translation = subprocess.check_output(['trans', f':{input_lang}', f':{output_lang}', text])
        translation = translation.decode()

        # Print the translated text to the console
        print(translation)

        # Speak the translated text
        self.text_to_speech(translation)

    def text_to_speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = Translator(root)
    root.mainloop()
