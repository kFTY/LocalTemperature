import urllib.request
from PIL import Image
import pytesseract

# Source
url = 'http://www.bgc-jena.mpg.de/wetter/Chart_T.gif'

# Download the image from the source

urllib.request.urlretrieve(url, 'tmp.gif')
# print ("downloading")

# Crop the image
img = Image.open("tmp.gif")
width = img.size[0]
height = img.size[1]
imgcrop = img.crop(
    (
        width - 140,
        3,
        width - 100,
        25
    )
)

img = imgcrop.convert("1")
img.save("imgcrop.gif")

# OCR the image

tmp = pytesseract.image_to_string(Image.open('imgcrop.gif'))
title = str('"The temperature outside is %s degree now."' % tmp)

# Output
print (title)
