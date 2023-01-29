import pytesseract
from PIL import Image
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

image = cv2.imread("test3.jpg")
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = get_grayscale(image)

print(pytesseract.image_to_string(image, lang = 'eng'))

