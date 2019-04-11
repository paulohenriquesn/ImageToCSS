import cv2
import numpy as cp
import pytesseract as ocr
from PIL
import Image

ocr.pytesseract.tesseract_cmd = r "PATH TESSERACT HERE"

phrase = ocr.image_to_string(Image.open('website.png'), lang = 'eng')

css_codes = phrase.split(";")
debug = []
execute = []
css = []

for i in css_codes:
  if i is not "":
  if "\n" in i:
  debug.append(i.replace("\n", ""))
else :
  debug.append(i)

def detectColor(input_):
  colors = ['red', 'blue']
if input_ in colors:
  return True
else :
  return False

def __interpreter(debug, css):
  if (debug is None):
    print("Error to read debug")
else :
  for i in range(len(debug)):
  if "#" in debug[i]:
  memory = debug[i].split(" ")
isAColor = detectColor(memory[1])
if isAColor == True:
  css.append(f "{memory[0]} " + "{" + f "color: {memory[1]}"
    "}")

__interpreter(debug, css)
f = open("main.css", "w+")
for i in css:
  f.write(f "{i}\r\n")
f.close()
print(css)
