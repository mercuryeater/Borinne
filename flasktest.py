import os

import tempfile
from flask import Flask, request, jsonify
from google_drive_auth import uploadImage


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
    # print(f'esto es el path de la imagen normal: {path}')

    # Aqui va la evaluacion del modelo para saber que hacer con la imagen
    # try:
        

    try:
        uploadImage(path)
    except Exception as e:
        print(f"Ocurrió un error al subir la imagen: {e}")
        return jsonify({"message": str(e)})

    return jsonify({'message': 'Imagen recibida correctamente'}), 200


app.run(host="0.0.0.0", port=80)
