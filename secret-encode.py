from PIL import Image
import numpy as np

message = "FLAG REDACTED" #hint: starts with 'acm{' and ends with '}'
src = "cat.png"
out = "normalcat.png"

i = 0
data = ""
for c in message:
    data += format(ord(c), "08b")
with Image.open(src) as img:
    width, height = img.size
    randx = np.random.randint(width/2)
    for x in range(0, width):
        for y in range(0, height):
            pixel = list(img.getpixel((x, y)))
            for n in range(0,3):
                if (i < len(data) and x >= randx):
                    pixel[n] = pixel[n] & ~1 | int(data[i])
                    i += 1
            img.putpixel((x,y), tuple(pixel))
    img.save(out, "PNG")