import os
from datetime import datetime


def octetToImage(binaryData):

    img = binaryData

    # Define el directorio de las imágenes
    image_dir = os.path.join(os.path.dirname(__file__), 'tempImages')

    # Verifica si el directorio existe, si no, créalo
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    current_time = datetime.now()
    file_name = current_time.strftime("%Y-%m-%d__%H_%M_%S") + ".jpg"

    # Define the full file path
    file_path = os.path.join(image_dir, file_name)

    try:
        with open(file_path, 'wb') as f:
            f.write(binaryData)
        print(f"Imagen guardada exitosamente en {file_path}")
        return f"Se guardo la imagen correctamente como {file_name}"
    except Exception as e:
        print(f"Ocurrió un error al guardar la imagen: {e}")
