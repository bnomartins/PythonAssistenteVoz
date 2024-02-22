from converterpdf import converterPDf
from convertermp3 import converterMp3
from downloadYoutube import Download

def utilities():
    while True:
            

        menu = input('''
        MENU: 
        Digite:
        1 - Converter em mp4 para mp3;
        2 - Download do vídeo do youtube;
        3 - Converter arquivo PDF para arquivo de texto;
        0 - Para SAIR
        ''')

        print(menu)

        if (menu == '1') : converterMp3()
        elif (menu == '2'): Download()
        elif (menu == '3'): converterPDf()
        elif (menu == '0'): exit()
        else : print("Opção Inválida!")

utilities()