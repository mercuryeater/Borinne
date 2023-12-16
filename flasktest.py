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
# I need to work on the model to recognize in worse conditions with worse type of images, similar background
# and worse light because it does not recognize Bob or it mistakenly classifies him as Corinne
#
# Also check what I'm returning so that can trigger another ESP32 device to drive Bob off or whatever


@app.route("/")
def index():
    return "Drink more coffee!"


@app.route("/test", methods=["POST"])
def test():

    path = octetToImage(request.data)

    try:
        result = categorize(path)

        if result == 0:
            try:
                uploadImage(path)
            except Exception as e:
                print(f"Ocurrió un error al subir la imagen: {e}")
                return jsonify({"message": str(e)})

            os.remove(path)
            print('Imagen de Bob recibida correctamente')
            return jsonify({'message': 'Imagen de Bob recibida correctamente', 'value': int(result)}), 200
        elif result == 1:
            try:
                uploadImage(path)
            except Exception as e:
                print(f"Ocurrió un error al subir la imagen: {e}")
                return jsonify({"message": str(e)})

            os.remove(path)
            print('Imagen de Corinne recibida correctamente')
            return jsonify({'message': 'Imagen de Corinne recibida correctamente', 'value': int(result)}), 200
        elif result == 2:
            os.remove(path)
            return jsonify({'message': 'No hay gatos en la imagen', 'value': int(result)}), 200
        else:
            return "Resultado desconocido"
    except Exception as e:
        print(f'Error: {e}')

    return jsonify({'message': 'data received'}), 200


app.run(host="0.0.0.0", port=80)
