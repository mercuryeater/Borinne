import tensorflow_hub as hub
import tensorflow as tf
from PIL import Image
import cv2
import numpy as np



loaded_model = tf.keras.models.load_model('BorinneV1.h5', custom_objects={
                          'KerasLayer': hub.KerasLayer})


def categorize(path):
    # Abrimos la imagen
    img = Image.open(path)

    # Nos aseguramos que reciba los 3 canales
    img = img.convert("RGB")

    # Normalizamos la imagen volviendola un array de numPy y la dividimos por 255
    img = np.array(img).astype(float)/255

    # redimensionamos la imagen para que sea lo que el modelo espera
    img = cv2.resize(img, (224, 224))

    prediction = loaded_model.predict(img.reshape(-1, 224, 224, 3))
    return np.argmax(prediction[0], axis=-1)


path = "c.jpg"

prediction = categorize(path)
print(prediction)