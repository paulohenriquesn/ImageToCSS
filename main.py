import cv2
import numpy as cp
import pytesseract as ocr
from PIL
import Image

ocr.pytesseract.tesseract_cmd = r "C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

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

def detectSizeModify(input_):
  if "pt" in input_:
  return True
else :
  return False

def detectHoverStart(input_):
  if "@hover" in input_:
  return True
else :
  return False

def detectHoverEnd(input_):
  if "hover@" in input_:
  return True
else :
  return False

def __interpreter(debug, css):
  inhover = False
if (debug is None):
  print("Error to read debug")
else :
  for i in range(len(debug)):
  if "#" in debug[i]:
  memory = debug[i].split(" ")
isAColor = detectColor(memory[1])
isASizeModify = detectSizeModify(memory[1])
isAStartHover = detectHoverStart(memory[1])
isaEndHover = detectHoverEnd(memory[1])
if isAStartHover == True:
  inhover = True
css.append(f "{memory[0]}:hover " + "{")
if isaEndHover == True:
  inhover = False
css.append("}")
if isASizeModify == True:
  if inhover == False:
  css.append(f "{memory[0]} " + "{" + f "font-size: {memory[1]}"
    "}")
else :
  css.append(f "font-size: {memory[1]}")
if isAColor == True:
  if inhover == False:
  css.append(f "{memory[0]} " + "{" + f "color: {memory[1]}"
    "}")
else :
  css.append(f "color: {memory[1]}")

__interpreter(debug, css)
f = open("main.css", "w+")
for i in css:
  f.write(f "{i}\r\n")
f.close()
print(css)
