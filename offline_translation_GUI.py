import os
import tkinter as tk
import pyttsx3
import subprocess
import speech_recognition as sr
import re

class Translator:
    def __init__(self, root):
        self.root = root
        self.root.title("Handheld Translator")

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

        # Create the text box for input text
        input_text_label = tk.Label(self.root, text="Input Text:")
        input_text_label.pack()
        self.input_text_box = tk.Text(self.root, height=5, width=50)
        self.input_text_box.pack()

        # Create the text box for output text
        output_text_label = tk.Label(self.root, text="Output Text:")
        output_text_label.pack()
        self.output_text_box = tk.Text(self.root, height=5, width=50)
        self.output_text_box.pack()

        # Create the speech recognition button
        self.recognize_button = tk.Button(self.root, text="Recognize", command=self.speech_recognition)
        self.recognize_button.pack()

        # Create the translate button
        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate)
        self.translate_button.pack()

        # Create the text-to-speech button
        self.text_to_speech_button = tk.Button(self.root, text="Speak", command=self.text_to_speech)
        self.text_to_speech_button.pack()

    def speech_recognition(self):
        # Use the speech recognizer to get the input text
        with sr.Microphone() as source:
            audio = self.r.listen(source)
        text = self.r.recognize_sphinx(audio)
        # Insert the input text into the input text box
        self.input_text_box.delete('1.0', tk.END)
        self.input_text_box.insert(tk.END, text)

    def translate(self):
        # Get the input and output languages from the dropdown menus
        input_lang = self.input_language_var.get()
        output_lang = self.output_language_var.get()

        # Get the input text from the input text box
        text = self.input_text_box.get('1.0', tk.END)

        # Use Translate-Shell to translate the text
        translation = subprocess.check_output(['wsl', 'trans', '-no-ansi', '-no-autocorrect', f':{input_lang}', f':{output_lang}', text])
        translation = translation.decode()

        # Extract the translated text from the translation output
        translated_text = re.search(r'\n\n([\s\S]*)\n\nTranslations', translation).group(1)

        # Insert the translation into the output text box
        self.output_text_box.delete('1.0', tk.END)
        self.output_text_box.insert(tk.END, translated_text.strip())

    def text_to_speech(self):
        # Get the output language from the dropdown menu
        output_lang = self.output_language_var.get()

        # Get the output text from the output text box
        text = self.output_text_box.get('1.0', tk.END)

        # Only speaks if there is text
        if text.strip():
            self.engine.setProperty('voice', f'{output_lang.lower()}')

            # Speak the output text
            self.engine.say(text)
            self.engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = Translator(root)
    root.mainloop()
