from googletrans import Translator
import Image
import pytesseract
s = [pytesseract.image_to_string(Image.open('text.jpg'),lang='eng')]
print(s)
trans =  Translator()
word_list = trans.translate(s,dest='mr')
for word in word_list :
	text=word.text
	marthi_text = text.encode("utf-8");
	print(marthi_text)
	obj_file = open("out.text","w")
	obj_file.write(marthi_text)



