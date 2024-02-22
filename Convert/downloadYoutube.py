# pip install pytube

from pytube import YouTube
from datetime import datetime
import os

def Download():
    link = input('Cole o link do vídeo para download :')
    print("Aguarde realizando download do vídeo")
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
        print('Download realizado')
    except:
        print("Some error occurred")
    print("Done")

