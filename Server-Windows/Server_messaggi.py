from chat_downloader import ChatDownloader
import subprocess
import os

from os import system
system("title " + "Server_Messaggi")
file1 = "risposta.txt"
# Cancella il file "risposta.txt" se esiste
if os.path.isfile(file1):
    os.remove(file1)
url = input("Inserisci link live: ")
with open('messaggi_youtube.json', 'w') as f:
    f.write('''
[
    {
        "action_type": "add_chat_item",
        "author": {
            "id": "UCV29Oa39B06hhHrOdgVQt0g",
            "images": [
                {
                    "id": "source",
                    "url": "https://yt4.ggpht.com/ytc/AGIKgqNPc5TM1_T0tN2R1VUAXpmMKbDdVAu68LKlYYHzMw"
                },
                {
                    "height": 32,
                    "id": "32x32",
                    "url": "https://yt4.ggpht.com/ytc/AGIKgqNPc5TM1_T0tN2R1VUAXpmMKbDdVAu68LKlYYHzMw=s32-c-k-c0x00ffffff-no-rj",
                    "width": 32
                },
                {
                    "height": 64,
                    "id": "64x64",
                    "url": "https://yt4.ggpht.com/ytc/AGIKgqNPc5TM1_T0tN2R1VUAXpmMKbDdVAu68LKlYYHzMw=s64-c-k-c0x00ffffff-no-rj",
                    "width": 64
                }
            ],
            "name": ""
        },
        "message": "Hey kawaii you are live. Introduce youself to our viewers :)!",
        "message_id": "CkUKGkNQWEI5SjNNeF80Q0ZjNE4xZ0FkZHh3QWVREidDT3JldlpuTXhfNENGY2pURVFnZGNtSUZXQTE2ODI1MTM3NzE5MzE%3D",
        "message_type": "text_message",
        "timestamp": 1682513772519466
    }
]''')
    
chat = ChatDownloader().get_chat(url, output="./messaggi_youtube.json")       # create a generator
subprocess.Popen(["start", "cmd", "/k", "python", "SELENIUMGPT_Emo.py"], shell=True)
for message in chat:                        # iterate over messages
    #chat.print_formatted(message) # print the formatted message
    # Analizza la stringa JSON e ottiene l'autore e il contenuto del messaggio
    author = message['author']['name']
    message = message['message']    
    userinput = '"' + author + ': ' + message +'"'
    print(userinput)





