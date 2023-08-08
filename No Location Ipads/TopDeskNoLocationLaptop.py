import pyautogui
import time
import keyboard
import pyperclip
#import cv2

debug = 0

while(debug):
    print(pyautogui.position())

def key_check():
    if (keyboard.is_pressed('esc')):
        exit()

f = open("NoLocation.txt")
f2 = open("finishedIpad.txt", "a")
f3 = open("unknownIpad.txt", "a")
school = "none"

key_check()
time.sleep (3)
key_check()

for x in f:
    ou = "null"
    text = "null"
    pyperclip.copy("null")

    if ("." in x):
        school = x[1:-1].lower()
        print(school)
        continue
    key_check()

    #refresh
    pyautogui.click(128, 73)
    key_check()
    time.sleep(4)
    key_check()
    #triple click to edit text
    pyautogui.click(300, 400)
    key_check()
    pyautogui.click(300, 400)
    key_check()
    pyautogui.click(300, 400)
    key_check()
    #searches service tag
    pyautogui.typewrite(x)
    key_check()
    pyautogui.press('enter')
    time.sleep(1)
    key_check()
    #highlight no assets text
    pyautogui.moveTo(725, 325)
    pyautogui.mouseDown()
    pyautogui.dragTo(810, 325)
    pyautogui.mouseUp()
    key_check()
    #copies text if exists
    pyautogui.hotkey('ctrl', 'c')
    text = pyperclip.paste().lower()
    key_check()
    #writes ipad s/n in unknownIpad text file
    if ("no" in text):
        f3.write(x)
        continue
    #click the device
    pyautogui.click(800, 380)
    key_check()
    time.sleep(6)
    key_check()
    #check if its in school
    pyautogui.click(1184, 425)
    time.sleep(3)
    #highlight location
    pyautogui.moveTo(525, 410)
    pyautogui.mouseDown()
    pyautogui.dragTo(740, 410)
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl', 'c')
    text = pyperclip.paste().lower()
    key_check()
    if (text not in school):
        print(text)
        #click the 'x'
        pyautogui.click(892, 121)
        time.sleep(1)
        pyautogui.click(892, 121)
        time.sleep(1)
        key_check()
        continue
    pyautogui.click(1192, 121)
    time.sleep(1)
    #click location
    #pyautogui.click(1450, 450)
    #key_check()
    #time.sleep(0.5)
    key_check()
    #click unassign
    pyautogui.click(1680, 315)
    key_check()
    time.sleep(0.5)
    #click unassign confirm
    pyautogui.click(1680, 420)
    key_check()
    time.sleep(0.5)
    key_check()
    #click assign room
    pyautogui.click(1355, 320)
    key_check()
    time.sleep(0.5)
    #click search box
    pyautogui.click(1400, 375)
    key_check()
    time.sleep(1)
    #search 'no location' location 
    pyautogui.typewrite("no location")
    key_check()
    time.sleep(1)
    key_check()
    pyautogui.press('enter')
    key_check()
    time.sleep(1)
    key_check()
    #click assign
    pyautogui.click(1700, 475)
    key_check()
    time.sleep(2)
    key_check()
    #click the 'x'
    pyautogui.click(892, 121)
    key_check()
    f2.write(x)
    time.sleep(2)

f.close()
f2.close()
f3.close()