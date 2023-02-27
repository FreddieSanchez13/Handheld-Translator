import tkinter as tk
from tkinter import ttk
import requests
import pocketsphinx
import googletrans
import pyttsx3
import speech_recognition as sr

class Translator:
    def __init__(self, root):
        self.root = root
        self.root.title("Handheld Translator")

        # Create the source language label and combobox
        self.source_label = ttk.Label(self.root, text="Original Language:")
        self.source_label.grid(row=0, column=0, padx=10, pady=10)
        self.source_combo = ttk.Combobox(self.root, values=["English", "Spanish", "French", "German", "Italian", "Portuguese"])
        self.source_combo.grid(row=0, column=1, padx=10, pady=10)

        # Create the target language label and combobox
        self.target_label = ttk.Label(self.root, text="Target Language:")
        self.target_label.grid(row=1, column=0, padx=10, pady=10)
        self.target_combo = ttk.Combobox(self.root, values=["English", "Spanish", "French", "German", "Italian", "Portuguese"])
        self.target_combo.grid(row=1, column=1, padx=10, pady=10)

        # Create the text to translate label and text field
        self.text_label = ttk.Label(self.root, text="Original Sentence:")
        self.text_label.grid(row=2, column=0, padx=10, pady=10)
        self.text_field = tk.Text(self.root, height=10, width=30)
        self.text_field.grid(row=2, column=1, padx=10, pady=10)

        # Create the translate button
        self.translate_button = ttk.Button(self.root, text="Translate", command=self.translate)
        self.translate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Create the translated text label and text field
        self.translated_label = ttk.Label(self.root, text="Original Sentence:")
        self.translated_label.grid(row=4, column=0, padx=10, pady=10)
        self.translated_field = tk.Text(self.root, height=10, width=30)
        self.translated_field.grid(row=4, column=1, padx=10, pady=10)
        # Create the speech recognition button
        self.speech_button = ttk.Button(self.root, text="Speak", command=self.speech_recognition)
        self.speech_button.grid(row=5,column=0, padx=10, pady=10)# Create the text-to-speech button
        self.tts_button = ttk.Button(self.root, text="Hear Sentence", command=self.text_to_speech)
        self.tts_button.grid(row=5, column=1, padx=10, pady=10)

    def speech_recognition(self):
        # Set the source language from the combobox
        self.source_language = self.source_combo.get()

        # Initialize the speech recognition object
        r = sr.Recognizer()

        # Set the language for the speech recognition
        r.language = self.source_language

        # Record audio using the default microphone
        with sr.Microphone() as source:
            audio = r.listen(source)

        # Convert the audio to text using pocketsphinx
        text = r.recognize_google(audio, language=self.source_language)

        # Insert the recognized text into the text field
        self.text_field.delete("1.0", "end")
        self.text_field.insert("1.0", text)

    def translate(self):
        # Get the source and target languages from the comboboxes
        source_language = self.source_combo.get()
        target_language = self.target_combo.get()

        # Get the text to translate from the text field
        text = self.text_field.get("1.0", "end")

        # Use the googletrans package to translate the text
        translated_text = googletrans.Translator().translate(text, src=source_language, dest=target_language).text

        # Insert the translated text into the translated text field
        self.translated_field.delete("1.0", "end")
        self.translated_field.insert("1.0", translated_text)

    def text_to_speech(self):
        # Get the target language from the combobox
        target_language = self.target_combo.get()

        # Get the translated text from the text field
        translated_text = self.translated_field.get("1.0", "end")

        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Set the voice and language for the text-to-speech engine
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.setProperty('language', target_language)

        # Speak the translated text
        engine.say(translated_text)
        engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = Translator(root)
    root.mainloop()