from gtts import gTTS
from playsound import playsound
import time
import pyautogui as pg
import os
import pyttsx3




import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

if __name__ == "__main__":
    speak = pyttsx3.init('sapi5')
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
# 
    def on_created(event):
        speak.say(f"O arquivo {event.src_path} foi criado !")
    def on_deleted(event):
        speak.say(f"O arquivo {event.src_path} foi deletado !")
    def on_modified(event):
        speak.say(f"O arquivo {event.src_path} foi modificado !")
    def on_moved(event):
        speak.say(f"O arquivo {event.src_path} foi movido !")

    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved

    path = '.'
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try: 
        while True:
            speak.runAndWait() 
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()