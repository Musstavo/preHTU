from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('test3.png')

result = decode(img)

print(result)