import urllib
from PIL import Image
import pytesseract
import os
# Source
url = 'http://www.bgc-jena.mpg.de/wetter/Chart_T.gif'

# Download the image from the source

urllib.urlretrieve(url, 'tmp.gif')
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
imgcrop.save("imgcrop.gif")

img = Image.open("imgcrop.gif").convert("L")
img.save("imgcrop.gif")
# OCR the image

tmp = pytesseract.image_to_string(Image.open('imgcrop.gif'))
print ("Temperature ouside: %s degree." % tmp)

os.system('/usr/bin/pushbullet.sh "Temperature outside: %s degree."' % tmp)
