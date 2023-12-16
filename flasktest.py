import os
from flask import Flask, request, jsonify
from google_drive_auth import uploadImage
from predict_app import categorize
from binaryHandling import octetToImage


app = Flask(__name__)

################################
# TO DO:
#
# Create a finally that althought the image is not uploaded the message saying image processed is sent
# and probably organize even more this code, it is still too spaghetti
#
# Also check what I'm returning so that can trigger another ESP32 device to drive Bob off or whatever


@app.route("/")
def index():
    return "Drink more coffee!"


@app.route("/test", methods=["POST"])
def test():

    path = octetToImage(request.data)

    messages = {
        0: 'Imagen de Bob recibida correctamente',
        1: 'Imagen de Corinne recibida correctamente',
        2: 'No hay gatos en la imagen'
    }

    try:
        result = categorize(path)

        if result in [0, 1]:
            try:
                uploadImage(path)
            except Exception as e:
                print(f"Ocurrió un error al subir la imagen: {e}")
            finally:
                os.remove(path)
                print(messages[result])
                return jsonify({'message': messages[result], 'value': int(result)}), 200
        elif result == 2:
            os.remove(path)
            return jsonify({'message': messages[result], 'value': int(result)}), 200
        else:
            return "Resultado desconocido"
    except Exception as e:
        print(f'Error: {e}')


app.run(host="0.0.0.0", port=80)
