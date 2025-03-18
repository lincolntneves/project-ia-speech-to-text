
# Extract Speech to Text
#pip install moviepy
#pip install SpeechRecognition
from moviepy import VideoFileClip
import speech_recognition as sr 

# Load the video 
video = VideoFileClip("O PRIMEIRO MILHÃO DO PABLO MARÇAL! #dinheiro #investimentos #cortes #pablomarcal #milionario #shorts [TKuBDdy4k0s].mp4") 

# Extract the audio from the video 
audio_file = video.audio 
audio_file.write_audiofile("test.wav") 

# Carregar o arquivo de áudio
file_path = "test.wav"  # Substitua pelo caminho do seu arquivo

recognizer = sr.Recognizer()

with sr.AudioFile(file_path) as source:
    audio_data = recognizer.record(source)  # Captura o áudio

# Converter áudio para texto usando a API do Google
try:
    text = recognizer.recognize_google(audio_data, language="pt-BR")  # Mudar idioma se necessário
    print("Texto transcrito:", text)
except sr.UnknownValueError:
    print("Não foi possível entender o áudio")
except sr.RequestError:
    print("Erro ao conectar à API do Google")
