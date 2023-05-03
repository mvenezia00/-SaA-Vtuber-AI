import time
import  json
import subprocess
import os
import play
from getaudiodev import getaudiodevice
from client_API import *

#05/04 simpleaudio in extensions/silero_tts/play.py. #modificato script silero per gestione nome output audio

from selenium import webdriver #da installare -- pip install seleniuim
from selenium.webdriver.chrome.service import Service # -- pip install webdriver_manager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from chat_downloader import ChatDownloader #da installare -- pip install chat-downloader

from os import system
system("title " + "Server_Principale")
 
##Avvio modello Emozioni
from transformers import pipeline
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False, device=None)

##Avvio pagina chrome per controllo Kawaii
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("http://localhost:7860/")

def invio_messaggio(userinput):
    #driver.find_element cerca i tasti o le caselle di testo nella pagina chrome aperta
    text_gen = driver.find_element(By.XPATH, "//button[normalize-space()='Text generation']")
    text_gen.click() #riporta su scheda chat (in caso modifico parametri e mi dimentico di tornare a scheda chat)
    generate = driver.find_element(By.ID, 'Generate')
    textbox = driver.find_element(By.CSS_SELECTOR, "div[id='component-5'] textarea[class='scroll-hide svelte-4xt1ch']")
    textbox.send_keys(userinput)
    generate.click()


def selenium_send(userinput):
    risposta_vecchia = get_risposta()
    invio_messaggio(userinput)
    risposta = get_risposta()
    while ((risposta == risposta_vecchia) or (risposta == "")):
        risposta = get_risposta()
        time.sleep(0.5)
    print(clean_risposta(risposta))
            ##VEDI CONCORRENZA
    #scrive risposta su file txt per essere inserita in overlay obs in chat.py
    start_time = time.time() 
    prediction = classifier(clean_risposta(risposta))
    print(prediction[0])
    get_audio()
    with open('risposta.txt', 'w', encoding='utf8') as f:
       f.write(clean_risposta(risposta))
    #avvia audio risposta
    filename = './messvocale.wav'
    play.voiceandface(prediction[0], filename, device) #filename = percorso+ nome file audio

userinput_old = ""
with open('risposta.txt', 'w') as f:
    f.write("")
device = getaudiodevice()
while(True):
    try : 
        f = open('messaggi_youtube.json')
        data = json.load(f)
        last_text = data[-1]
        author = last_text['author']['name']
        message = last_text['message']
        userinput = '"' + author + ': ' + message +'"'
        f.close()
    except :
        print ("MARIO è SCEMO")
    if(userinput != userinput_old):
        print(userinput)
        selenium_send(userinput)
        userinput_old = userinput




