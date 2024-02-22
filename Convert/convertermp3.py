import os
from moviepy.editor import *
import glob

def converterMp3():
    lista_mp4 = glob.glob("*.mp4")

    if len(lista_mp4) > 0:
        for video in lista_mp4:
            print('Lendo arquivo mp4')
            print('-'*20)
            mp4 = VideoFileClip(os.path.join(video))
            nome_mp3 = video[:-4]+'.mp3'

            print('Convertendo para mp3')
            mp4.audio.write_audiofile(os.path.join(nome_mp3))
            print('-'*20)
            print('Converteu mp4 '+video+' para mp3 '+nome_mp3)

    else: 
        print('Não existem arquivos mp4 para converter, favor disponibilizar na pasta o arquivo e tentar novamente')