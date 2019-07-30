from PIL import Image
import pytesseract
import cv2
import os

def run_ocr(image):
	try:
		image = cv2.imread(image)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		filename = "{}.png".format(os.getpid())
		cv2.imwrite(filename, gray)
		text = pytesseract.image_to_string(Image.open(filename))
		os.remove(filename)
		return text
	except:
		print("error with OCR")

