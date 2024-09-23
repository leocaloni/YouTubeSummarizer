import pytubefix as pt
import ffmpeg
import whisper
import openai

#pega o link do yt
yt_str = input("Digite o link do vídeo: ")
yt = pt.YouTube(yt_str)

#converte para áudio
filename = "audio.wav"
try:
    stream = yt.streams.filter(only_audio=True).first().url
    ffmpeg.input(stream).output(filename, format = 'wav', loglevel="error").run()
except Exception as e:
    print(f"Erro durante a conversão: {e}")

#transcrição
try:
    model = whisper.load_model("base")
    audio_file = whisper.load_audio(filename)
    result = model.transcribe(audio_file, language="en")
    print(result["text"])
except FileNotFoundError:
    print(f"Arquivo do audio {filename} não encontrado")
except Exception as e:
    print(f"Erro durante a transcrição: {e}")
