from rembg import remove
from PIL import Image

input_path = 'photo_love4.jpg'
output_path = 'photo_loved4.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
