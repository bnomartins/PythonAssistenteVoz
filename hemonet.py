# -*- coding: utf-8 -*-

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import time
import pyautogui as pg
import os
import pyttsx3
from Piadas import piadas
from inspiracao import inspiracao
from datetime import datetime, timedelta

from Apresentacao import slideAnterior, slidePosterior, modoApresentacao, encerrar, abaAnterior, abaPosterior, minimizar, iniciar, slideTop, slideBottom, slideNextAba, slideBeforeAba, slideAccecp, slideAceitar, encerrarTela
from MonitorTemperatura import verificar_temperatura
from MonitorSite import verificar_site
from Despertador import despertador

from subprocess import Popen

import webbrowser

if __name__ == "__main__":

    def ouvir_microfone():

        cont = 0

        speak = pyttsx3.init()
        # speak.setProperty('voice', 'portugal')
        speak.setProperty("rate", 280)
        # voices = speak.getProperty('voices')
        # speak.setProperty("voice", voices[0].id)


        #Habilita o microfone para ouvir o usuario
        microfone = sr.Recognizer()

        with sr.Microphone() as source:

            iniciado = 0
            iniciado_temp = 0
            temp = verificar_temperatura()[0]
            hum = verificar_temperatura()[1]

            while True:
                speak.runAndWait() 
                tempoagora = datetime.now()

                                                                                                 
                # iniciação
                if (iniciado == 0):

                    # webbrowser.open(f'https://site.com/monitoramento/Assistente iniciado e disponível,A temperatura da sala do datacenter está em {temp} graus celsius e a umidade está em {hum} por cento/2399368517623')

                    speak.say(f"Assistente iniciado e disponível!")
                    speak.runAndWait()  
                    # speak.say(f"A temperatura da sala está em {temp} graus celsius e a umidade está em {hum} por cento!")
                    # # speak.say(f"Um novo chamado!")
                    iniciado = 1

                    # os.startfile("monitoramento.bat")

                
                # Monitoramento de temperatura
                if float(temp) > float(23.0) and cont in (5, 10, 20, 30, 40, 50) and iniciado_temp < 1:
                    monitor = verificar_temperatura()
                    speak.say(f"A sala do Datacenter está em {temp} graus célsius e {hum} por cento de humidade relativa do ar")   
                    iniciado_temp = 1
                
                # Monitoramento de umidade
                if float(hum) > float(70.0) and cont in (5, 10, 20, 30, 40, 50) and iniciado_temp < 1:
                    monitor = verificar_temperatura()
                    speak.say(f"A sala do Datacenter está em {temp} graus célsius e {hum} por cento de humidade relativa do ar")   
                    iniciado_temp = 1

                                
                # # Despertador
                # if despertador(8, 0, 0, 20):
                #     webbrowser.open(f'https://site.com/monitoramento/Bom dia, time, já são oito horas, a temperatura da sala do datacenter está em {temp} graus celsius e a umidade está em {hum} por cento/2399368517623')
                #     iniciado_temp = 0
                                
                # # Despertador
                # if despertador(12, 0, 0, 20):
                #     webbrowser.open(f'https://site.com/monitoramento/Boa tarde, time, já são meio dia, a temperatura da sala do datacenter está em {temp} graus celsius e a umidade está em {hum} por cento/2399368517623')
                #     iniciado_temp = 0
                                
                # # Despertador
                # if despertador(13, 0, 0, 20):
                #     webbrowser.open(f'https://site.com/monitoramento/Boa tarde, time, já são treze horas, a temperatura da sala do datacenter está em {temp} graus celsius e a umidade está em {hum} por cento/2399368517623')
                #     iniciado_temp = 0
                                
                # # Despertador
                # if despertador(14, 0, 0, 20):
                #     webbrowser.open(f'https://site.com/monitoramento/Boa tarde, time, já são quatorze horas, a temperatura da sala do datacenter está em {temp} graus celsius e a umidade está em {hum} por cento/2399368517623')
                #     iniciado_temp = 0
                                                               
                # # Despertador
                # if despertador(16, 0, 0, 20):
                #     webbrowser.open(f'https://site.com/monitoramento/Boa tarde, time, já são dezesseis horas, a temperatura da sala do datacenter está em {temp} graus celsius e a umidade está em {hum} por cento/2399368517623')
                #     iniciado_temp = 0
                                                                
                # # Despertador
                # if despertador(18, 0, 0, 20):
                #     webbrowser.open(f'https://site.com/monitoramento/Boa tarde, time, já são dezoito horas, a temperatura da sala do datacenter está em {temp} graus celsius e a umidade está em {hum} por cento/2399368517623')
                #     iniciado_temp = 0
                
                microfone.adjust_for_ambient_noise(source)              
                try:
                    audio = microfone.listen(source)
                    frase = microfone.recognize_google(audio, language='pt-BR')
                
                    frasemin = frase.lower()

                    if 'assistente como está a sala do data center' in frasemin or 'assistente data center' in frasemin :
                        speak.say(f"A sala do Datacenter está em {temp} graus célsius e {hum} por cento de humidade relativa do ar")   

                    if 'assistente apresentação' in frasemin or 'assistente apresentação' in frasemin :
                        minimizar()
                        time.sleep(1)
                        os.startfile("S:\\pasta\\arquivo.txt.ods")
                        time.sleep(2)
                        slideAccecp()

                    if 'assistente fechar' in frasemin:
                        time.sleep(2)
                        encerrarTela()

                    if 'assistente aceitar' in frasemin or 'assistente aceitar' in frasemin :
                        slideAceitar()

                    if 'assistente próximo' in frasemin or 'assistente próximo' in frasemin :
                        slideNextAba()

                    if 'assistente anterior' in frasemin or 'assistente anterior' in frasemin :
                        slideBeforeAba()

                    if 'assistente em cima' in frasemin or 'assistente em cima' in frasemin :
                        slideTop()

                    if 'assistente embaixo' in frasemin or 'assistente embaixo' in frasemin :
                        slideBottom()

                        # webbrowser.open(f'https://site.com/monitoramento/assistente de apresentação iniciado/2399368517623')

                    # if 'próximo por favor' in frasemin or 'assistente próximo' in frasemin :
                    #     slidePosterior()

                    # if 'anterior por favor' in frasemin or 'assistente anterior' in frasemin :
                    #     slideAnterior()

                    # if 'encerrar por favor' in frasemin or 'assistente encerrar' in frasemin  or 'assistente fechar' in frasemin :
                    #     encerrar()

                    if 'assistente piadas' in frasemin or 'assistente piada' in frasemin or 'hemomed piadas' in frasemin or 'hemomed piada' in frasemin or 'assistente encerrar com chave de ouro' in frasemin:
                        # piadaEscolhida = random.choice(piadas)
                        # print(piadaEscolhida)
                        print('O que o pato disse para a pata? ve Quá Quá Quá')

                        speak.say('O que o pato disse para a pata?')
                        time.sleep(2)
                        speak.say('vem Quá Quá Quá, kakakaká kákákakaka')
                        speak.runAndWait()

                    if 'assistente menu' in frasemin or 'assistente menu' in frasemin or 'hemomed menu' in frasemin or 'hemomed menu' in frasemin:
                        piadaEscolhida = """
                            Os comandos disponíveis são 
                            Para apresentar: assistente apresentação, assistente próximo, assistente anterior e assistente encerrar,
                            Para utilitários: assistente conversão, assistente download,
                            Para usar chat gpt: assitente pergunta, assistente o que é
                        """
                        print(piadaEscolhida)
                        speak.say(piadaEscolhida)
                        speak.runAndWait()

                    if 'assistente pergunta' in frasemin or 'uma pergunta' in frasemin:
                        from OpenAI.IntegrarChatGPT import generate_text

                        pergunta = frasemin.split('assistente o que é')
                        pergunta = frasemin.split('assistente quanto é')
                        r = generate_text(pergunta)
                        speak.say(f"Pergunta: {pergunta}")     
                        speak.say(f"Resposta: {r}")     
                        speak.runAndWait()    

                    if 'assistente frase motivacional' in frasemin or 'assistente motivação' in frasemin or 'hemomed pílula motivacional' in frasemin or 'hemomed motivação' in frasemin:
                        # inspiracaoEscolhida = random.choice(inspiracao)
                        # speak.say(inspiracaoEscolhida)     
                        speak.say('Existe um momento na vida de cada pessoa que é possível sonhar e realizar nossos sonhos… e esse momento tão fugaz chama-se presente e tem a duração do tempo que passa. De Mário Quitana')	     
                        speak.runAndWait()    

                   
                    if 'assistente qual o número do almoxarifado' in frasemin or 'hemomet qual o número do almoxarifado' in frasemin or 'qual o número do almoxarifado' in frasemin:
                        speak.say('Ramal setenta e nove, zero um')
                        speak.say('Ramal setenta e nove, zero um')
                        speak.runAndWait()                                                                     


                        # speak.say("Os números provaveis da mega sena são ") #(64) 3441-4013 / (64) 3411-3730
                        # for i in r:
                        #     print(i)
                        #     speak.say(i) #(64) 3441-4013 / (64) 3411-3730
                        #     speak.runAndWait()         
                        
                        # speak.say("Repetindo") #(64) 3441-4013 / (64) 3411-3730
                        # for i in r:
                        #     print(i)
                        #     speak.say(i) #(64) 3441-4013 / (64) 3411-3730
                        #     speak.runAndWait()        

                    print(frase)
                                
                except LookupError:
                    print(f'1 - Não Entendi {cont}')
                    print(tempoagora)

                except sr.UnknownValueError as e:
                    print(f'2 - Valor Inválido {cont}')
                    print(tempoagora)

                except KeyboardInterrupt:
                    print('keyboard interrupt')
                    print(tempoagora)
                    
                except:
                    print(f'{cont}')
                    print(tempoagora)
                cont +1


    ouvir_microfone()