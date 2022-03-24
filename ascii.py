from PIL import Image, ImageDraw, ImageFont

import math

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

scalefactor = 0.2

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

text_file = open("Output.txt", "w")

im = Image.open("cran.png")

width, height = im.size
im = im.resize((int(scalefactor*width), int(scalefactor*height)), Image.NEAREST)
width, height = im.size
pix = im.load()

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))

    text_file.write('\n')

im.save('output.png')
