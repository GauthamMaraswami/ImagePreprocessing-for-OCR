from googletrans import Translator
from PIL import Image
import pytesseract
import argparse
import cv2
import os

# load the example image and convert it to grayscale
image = cv2.imread("text.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


gray = cv2.medianBlur(gray, 3)
 
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
text = "{}.jng".format(os.getpid())
cv2.imwrite('tesxt.jpg', gray)


s = [pytesseract.image_to_string(Image.open('text.jpg'),lang='eng')]
print(s)

trans =  Translator()
word_list = trans.translate(s,dest='kn')
for word in word_list :
	text=word.text
	marthi_text = text.encode("utf-8");
	print(marthi_text)
	obj_file = open("out.text","w")
	obj_file.write(marthi_text)



