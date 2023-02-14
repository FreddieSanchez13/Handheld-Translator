import tkinter as tk
from tkinter import ttk
import requests
import googletrans
import pyttsx3
import speech_recognition as sr

class Translator:
    def __init__(self, root):
        self.root = root
        self.root.title("HandHeld Translator")

        #create the source language label and combobox
        self.source_label = ttk.Label(self.root, text = "Original Language:")
        self.source_label.grid(row=0, column = 0, padx = 10, pady = 10)
        self.source_dropdown = ttk.Combobox(self.root, values = ["English", "Spanish", "French", "German", "Italian", "Portuguese"])
        self.source_dropdown.grid(row=0, column = 1, padx = 10, pady = 10)

        #create the source language label and combobox
        self.translated_label = ttk.Label(self.root, text = "Target Language:")
        self.translated_label.grid(row=1, column = 0, padx = 10, pady = 10)
        self.translated_dropdown = ttk.Combobox(self.root, values = ["English", "Spanish", "French", "German", "Italian", "Portuguese"])
        self.translated_dropdown.grid(row=1, column = 1, padx = 10, pady = 10)

        #create the text to translate label and field
        self.text_label = ttk.Label(self.root, text = "Original Sentence:")
        self.text_label.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.text_field = tk.Text(self.root, height = 10, width = 30)
        self.text_field.grid(row = 2, column = 1, padx = 10, pady = 10)

        #create translate button
        self.translate_button = ttk.Button(self.root, text = "Translate", command = self.translate)
        self.translate_button.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 10)

        #create the text to translate label and field
        self.translated_label = ttk.Label(self.root, text = "Original Sentence:")
        self.translated_label.grid(row = 4, column = 0, padx = 10, pady = 10)
        self.translated_field = tk.Text(self.root, height = 10, width = 30)
        self.translated_field.grid(row = 4, column = 1, padx = 10, pady = 10)
        
        #create the sppech recognition and text to speech buttons
        self.speech_button = ttk.Button(self.root, text = "Speak", command = self.speech_recognition)
        self.speech_button.grid(row = 5, column = 0, padx = 10, pady = 10)
        self.tts_button = ttk.Button(self.root, text = "Hear Sentence", command = self.text_to_speech)
        self.tts_button.grid(row = 5, column = 1, padx = 10, pady = 10)

    def speech_recognition(self):
        #set the source language form the dropbox
        self.source_language = self.source_dropdown.get()

        #initialize the speech recognition object
        r = sr.Recognizer()

        #set the language for the speech recognition
        r.language = self.source_language

        #record audio using the default microphone
        with sr.Microphone() as source:
            audio = r.listen(source)
        
        #convert audio file to text
        text = r.recognize_google(audio, language = self.source_language)

        #insert recognized text into appropriate field
        self.text_field.delete("1.0", "end")
        self.text_field.insert("1.0", text)

    def translate(self):
        #get the source and target languages
        source_language = self.source_dropdown.get()
        target_language = self.translated_dropdown.get()

        #get the text to be translated
        text = self.text_field.get("1.0", "end")

        #use googletrans to translate
        translated_text = googletrans.Translator().translate(text, src = source_language, dest = target_language).text

        #insert the translated text to appropriate field
        self.translated_field.delete("1.0", "end")
        self.translated_field.insert("1.0", translated_text)

    def text_to_speech(self):
        #get the target language from the dropbox
        target_language = self.translated_dropdown.get()

        #get the translated text from the field
        translated_text = self.translated_field.get("1.0", "end")

        #initialize the text to speech engine
        engine = pyttsx3.init()

        #set the voice and language for tts
        voices = engine.getProperty('voices')
        engine.setProperty('voices', voices[1].id)
        engine.setProperty('language', target_language)

        #speak the translated text
        engine.say(translated_text)
        engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = Translator(root)
    root.mainloop()




