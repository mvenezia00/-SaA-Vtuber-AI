import requests ##da installare
import os 
import io
from pydub import AudioSegment ##da installare
import json

def get_risposta():    
    x = requests.get('http://127.0.0.1:5000/risposta')
    return(x.content)

def clean_risposta(rispostanc):

    response = rispostanc

    # Rimuove i caratteri di newline dalla risposta
    response = response.strip()

    # Decodifica la risposta come stringa
    response_str = response.decode('utf-8')

    # Parsa la stringa JSON in un dizionario Python
    response_dict = json.loads(response_str)

    # Stampa il valore associato alla chiave 'message'
    response_str = str(response_dict['message'])

    return(response_str)

def get_audio():
    url = 'http://localhost:5000/audio'
    response = requests.get(url)

    with open('messvocale.wav', 'wb') as f:
        f.write(response.content)
