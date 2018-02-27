
from PIL import Image
import pytesseract
import argparse
import cv2
import os
from googletrans import Translator
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", gray)

# check to see if we should apply thresholding to preprocess the
# image
if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# make a check to see if median blurring should be done to remove
# noise
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)


s = [pytesseract.image_to_string(Image.open(filename),lang='eng')]
print(s)
os.remove(filename)
trans =  Translator()
word_list = trans.translate(s,dest='kn')
for word in word_list :
	text=word.text
	marthi_text = text.encode("utf-8");
	print(marthi_text)
	obj_file = open("out.text","w")
	obj_file.write(marthi_text)







