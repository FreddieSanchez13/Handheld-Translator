import pyaudio
from pocketsphinx import LiveSpeech, get_model_path

# Set up the audio input stream
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

# Set up the PocketSphinx recognizer
model_path = get_model_path()
speech = LiveSpeech(
     verbose = False,
     sampling_rate = 16000,
     buffer_size = 2048,
     no_search = False,
     full_utt = False,
     hmm = model_path + '/en-us',
     lm = model_path + '/en-us.lm.bin',
     dic = model_path + '/cmudict-en-us.dict'
)

# Start the recognizer and process audio input
for phrase in speech:
    print(phrase)

# Get the recognized words and print them
stream.stop_stream()
stream.close()
audio.terminate()