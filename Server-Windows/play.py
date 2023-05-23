import os
import time
import wave
import pyautogui#da installare -- pip install pyautoguy
pyautogui.FAILSAFE = False
import sounddevice as sd  #pip install sounddevice
import soundfile as sf  #pip install pysoundfile
import logging
import random
import datetime

#prediction = emotion

def voiceandface(prediction, filename, device, r):
    set_face(prediction, r = r)
    play_audio(filename = filename, device = device)
    time.sleep(1)
    set_idle()

def set_face(prediction, r):
    risp = r.lower()
    if ((' meow' in risp) or (' \"meow' in risp) or (' \"miao' in risp) or (' miao' in risp) or (' purr' in risp) or (' \"purr' in risp) or (' \"rawr' in risp) or (' rawr' in risp)):
        pyautogui.keyDown('shift')
        pyautogui.keyDown('f4')
        pyautogui.keyUp('f4')
        pyautogui.keyUp('shift')
            
    elif(prediction['label'] == 'joy') :
        pyautogui.keyDown('shift')
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('f8')
        pyautogui.keyUp('f8')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')

            
    elif(prediction['label'] == 'sadness') :
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.keyDown("f6")
        pyautogui.keyUp("f6")
        pyautogui.keyUp("shift")
        pyautogui.keyUp("ctrl")

    elif(prediction['label'] == 'fear') :
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.keyDown("f6")
        pyautogui.keyUp("f6")
        pyautogui.keyUp("shift")
        pyautogui.keyUp("ctrl")

    elif(prediction['label'] == 'anger') :
        pyautogui.keyDown('shift')
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('f4')
        pyautogui.keyUp('f4')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('ctrl')

    elif(prediction['label'] == 'surprise') :
        pyautogui.keyDown('shift')
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('f7')
        pyautogui.keyUp('f7')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('ctrl')

def set_idle():
        # Ottenere la data e l'ora attuali
        now = datetime.datetime.now()
        # Utilizzare la data e l'ora come seed per la generazione casuale
        random.seed(now)
        random_number = random.randint(1, 2)
        if (random_number == 1):
            pyautogui.keyDown('shift')
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('f2')
            pyautogui.keyUp('shift')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('f2')
        else:
            pyautogui.keyDown('shift')
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('f5')
            pyautogui.keyUp('shift')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('f5')            

def play_audio(filename, device):
    try:
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data, fs, device=device, blocking=True)
        status = sd.get_status()
        if status:
            logging.warning(str(status))
        sd.wait()
    except KeyboardInterrupt:
        print('\nInterrupted by user')
    except Exception as e:
        print(type(e)._name_ + ': ' + str(e))

