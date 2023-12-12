import os
import PIL.Image as Image
import io
import base64
from byte_array import byte_data


def octetToImage(octet):
    binaryOctet = base64.b64decode(octet)
    imgOctet = Image.open(io.BytesIO(binaryOctet))
    imgOctet.save(os.path.join(os.path.dirname(
        __file__), 'tempImages', 'imageOctet.png'))


# b = base64.b64decode(byte_data)
# # base64 lo convierte en un binary string
# # print(b)
# img = Image.open(io.BytesIO(b))
# img.show()
# # Ya esta la imagen que podria guardarse con
# img.save(os.path.join(os.path.dirname(__file__), 'tempImages', 'imageTest.png'))

b = byte_data

with open('image.jpg', 'wb') as f:
    f.write(b)
