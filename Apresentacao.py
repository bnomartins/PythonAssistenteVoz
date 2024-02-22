import pyautogui as pg
import time
# pg.displayMousePosition()

def slideAnterior():
    pg.press('left')
    time.sleep(1)

def slideAceitar():
    pg.press('enter')
    time.sleep(1)

def slideAccecp():
    pg.press('enter')
    time.sleep(1)

def slidePosterior():
    pg.press('right')
    time.sleep(1),

def slideTop():
    pg.press('pageup')
    time.sleep(1),

def slideBottom():
    pg.press('pagedown')
    time.sleep(1),

def slideNextAba():
    pg.hotkey('ctrl', 'tab')
    time.sleep(1),

def slideBeforeAba():
    pg.hotkey('ctrl', 'shift', 'tab')
    time.sleep(1),

def minimizar():
    pg.hotkey('win', 'm')
    time.sleep(2)

def modoApresentacao():
    pg.press('f5')
    time.sleep(1)
    
def encerrarTela():
    time.sleep(1)
    pg.hotkey('alt', 'f4')
    slideAceitar()
    
def encerrar():
    pg.press('esc')
    time.sleep(1)
    pg.hotkey('alt', 'f4')
    iniciar()

def iniciar():
    pg.hotkey('win', '1')
    
def abaPosterior():
    pg.hotkey('ctrl', 'tab')
    
def abaAnterior():
    pg.hotkey('ctrl', 'shift', 'tab')
