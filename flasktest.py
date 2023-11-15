import os

from flask import Flask, request, jsonify
from google_drive_auth import uploadImage
from predict_app import categorize


app = Flask(__name__)


@app.route("/")
def index():
    return "Drink more coffee!"


@app.route("/upload", methods=["POST"])
def post_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part in the request'}), 400

    img = request.files['image']
    # Aquí puedes procesar la imagen como desees
    # Por ejemplo, podrías guardarla en un archivo:
    img.save(os.path.join(os.path.dirname(__file__), 'tempImages', img.filename))

    path = os.path.join(os.path.dirname(__file__), 'tempImages', img.filename)

    # Aqui va la evaluacion del modelo para saber que hacer con la imagen
    try:
        result = categorize(path)

        if result == 0:
            try:
                uploadImage(path)
            except Exception as e:
                print(f"Ocurrió un error al subir la imagen: {e}")
                return jsonify({"message": str(e)})

            os.remove(path)
            return jsonify({'message': 'Imagen de Bob recibida correctamente', 'value': int(result)}), 200
        elif result == 1:
            try:
                uploadImage(path)
            except Exception as e:
                print(f"Ocurrió un error al subir la imagen: {e}")
                return jsonify({"message": str(e)})

            os.remove(path)
            return jsonify({'message': 'Imagen de Corinne recibida correctamente', 'value': int(result)}), 200
        elif result == 2:
            os.remove(path)
            return jsonify({'message': 'No hay gatos en la imagen', 'value': int(result)}), 200
        else:
            return "Resultado desconocido"
    except Exception as e:
        print(f'Error: {e}')


app.run(host="0.0.0.0", port=80)
