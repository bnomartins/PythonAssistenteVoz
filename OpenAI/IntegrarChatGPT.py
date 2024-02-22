import os
import openai
import pyttsx3

# -*- coding: utf-8 -*-py
#instalar o pyaudio  pip install pipwin pelo pipwin e depois instalar usando python -m pipwin pyaudio
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

from datetime import datetime

openai.api_key = '###Sua Key Aqui###'

def generate_text(prompt):
    print(datetime.now())
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=256,
    n=1,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    
    message = response.choices[0].text
    return message
    print(datetime.now())


def emitir(pergunta, resposta):
    speak = pyttsx3.init()

    speak.say(f"pergunta: {pergunta}")
    speak.say(f"resposta: {resposta}")
    speak.runAndWait()  
    print(datetime.now())



prompt = input('Faça a sua pergunta \n')
r = generate_text(prompt)
emitir(prompt, r)