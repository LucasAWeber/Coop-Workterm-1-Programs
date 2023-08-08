import pyautogui
import time
import keyboard
import pyperclip
#import cv2

#while(True):
    #print(pyautogui.position())

def key_check():
    if (keyboard.is_pressed('esc')):
        exit()

f = open("Displaced.txt")
f2 = open("finished.txt", "a")
school = "none"

key_check()
time.sleep (2)
key_check()

for x in f:
    ou = "Displaced"
    if ("." in x):
        school = x[1:-1].lower()
        print(school)
        continue
    key_check()
    #refresh
    pyautogui.click(-1800, 360)
    key_check()
    time.sleep(2)
    key_check()
    #service tag search
    pyautogui.click(-1030, 305)
    key_check()
    time.sleep(0.5)
    key_check()
    #triple click to edit text
    pyautogui.click(-1000, 380)
    key_check()
    pyautogui.click(-1000, 380)
    key_check()
    pyautogui.click(-1000, 380)
    key_check()
    #searches service tag
    pyautogui.typewrite(x)
    key_check()
    pyautogui.press('enter')
    key_check()
    time.sleep(2.2)
    key_check()
    #highlight school
    if (len(x) > 16):
        pyautogui.moveTo(-805, 415)
        pyautogui.mouseDown()
        pyautogui.dragTo(-750, 415)
        pyautogui.mouseUp()
    else:
        pyautogui.moveTo(-865, 415)
        pyautogui.mouseDown()
        pyautogui.dragTo(-800, 415)
        pyautogui.mouseUp()
    #copy school
    pyautogui.hotkey('ctrl', 'c')
    ou = pyperclip.paste().lower()
    print(ou)
    if (school not in ou and "chromebooks" not in ou):
        continue
    #click checkbox of service tag
    pyautogui.click(-1205, 415)
    key_check()
    #click move
    pyautogui.click(-1000, 250)
    key_check()
    time.sleep(1)
    key_check()
    #searches displaced ou
    pyautogui.typewrite("Displaced Chromebooks")
    key_check()
    time.sleep(2)
    key_check()
    #clicks displaced ou
    pyautogui.click(-1000, 690)
    key_check()
    time.sleep(1)
    key_check()
    #click move
    pyautogui.click(-710, 770)
    key_check()
    f2.write(x)
    key_check()
    time.sleep(4)

f.close()
f2.close()
