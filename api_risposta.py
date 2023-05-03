from flask import Flask, make_response
from flask_restful import Resource, Api, reqparse
import ast
app = Flask(__name__)
api = Api(app)

class Risposta(Resource):
    def get(self):
        try:
            with open('risposta.txt', 'r') as f:
                messaggio = f.read()
            return {'message' : messaggio}, 200  # return data and 200 OK code
        except:
            return {'message' : "messaggio non creato"}, 666  # return data and 200 OK code
    pass

class Audio(Resource):
    def get(self):
        # qui si dovrebbe aggiungere la logica per determinare quale file inviare in base alla richiesta GET
        # qui, per esempio, si sta inviando il file "example.wav" dal path di sistema "/path/to/example.wav"
        with open('./extensions/silero_tts/outputs/messvocale.wav', "rb") as audio_file:
            audio_bytes = audio_file.read()
        response = make_response(audio_bytes)
        response.headers.set("Content-Type", "audio/wav")
        response.headers.set(
            "Content-Disposition", "attachment", filename="messvocale.wav"
        )
        return response
    
api.add_resource(Audio, '/audio')  # '/users' is our entry point for Users
api.add_resource(Risposta, '/risposta')  # '/users' is our entry point for Users

if __name__ == '__main__':
    app.run()  # run our Flask app



