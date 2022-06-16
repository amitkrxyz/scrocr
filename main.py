import os
from PIL import Image
import time
import pyautogui
import pytesseract

WAIT_TIME = 5
for i in range(WAIT_TIME):
    print(f"Selecting top left part of screen in {WAIT_TIME - (i+1)} seconds...")
    time.sleep(1)
print("Done\n")

left, top = pyautogui.position()

for i in range(WAIT_TIME):
    print(f"Selecting bottom right part of screen in {WAIT_TIME - (i+1)} seconds...")
    time.sleep(1)
print("Done\n")

right, bottom = pyautogui.position()

width = right - left
height = bottom - top

im = pyautogui.screenshot(region=(left,top, width, height))
#im.save('temp.png')
text = pytesseract.image_to_string(im)
print("Result: \n")
print(text.strip())
