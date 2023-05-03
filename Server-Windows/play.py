import os
import time
import wave
import pyautogui#da installare -- pip install pyautoguy
pyautogui.FAILSAFE = False
import sounddevice as sd  #pip install sounddevice
import soundfile as sf  #pip install pysoundfile
import logging
#prediction = emotion


def voiceandface(prediction, filename, device):
    set_face(prediction)
    play_audio(filename = filename, device = device)
    time.sleep(1)
    set_default_face()

def set_face(prediction):
    if(prediction['label'] == 'joy') :
        pyautogui.keyDown('shift')
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('f4')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('f4')
             
    elif(prediction['label'] == 'sadness') :
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.keyDown("f5")
        pyautogui.keyUp("f5")
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
        pyautogui.keyDown('f3')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('f3')

    elif(prediction['label'] == 'surprise') :
        pyautogui.keyDown('shift')
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('f6')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('f6')

    elif(prediction['label'] == "neutral"):
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.keyDown("f1")
        pyautogui.keyUp("f1")
        pyautogui.keyUp("shift")
        pyautogui.keyUp("ctrl")

def set_default_face():
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.keyDown("f1")
        pyautogui.keyUp("f1")
        pyautogui.keyUp("shift")
        pyautogui.keyUp("ctrl")




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

