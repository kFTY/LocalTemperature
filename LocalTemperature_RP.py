import urllib
from PIL import Image
import pytesseract
import os
import telegram
# Source
url = 'http://www.bgc-jena.mpg.de/wetter/Chart_T.gif'


def push_to_phone(txt):
    txt = str(txt)
    TOKEN="498010819:AAHLAphkWugooms4lRIhHUyTfYXxfGk6DhM"
    bot = telegram.Bot(token=TOKEN)
    CHATID="146500374"
    bot.send_message(chat_id=CHATID, text=txt)


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

push_to_phone("Temperature outside: %s degree." % tmp)
os.system('rm tmp.gif')
os.system('rm imgcrop.gif')
