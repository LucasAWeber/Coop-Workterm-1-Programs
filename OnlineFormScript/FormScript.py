import pyautogui
import time
import keyboard

#https://www.thatsuitemoney.ca/en/application-k12

#while(True):
    #print(pyautogui.position())

def key_check():
    if (keyboard.is_pressed('esc')):
        exit()

f = open("UGDSB-Microsoft Settlement.csv")
f2 = open("finished.txt","a")

time.sleep(3)
first_line = f.readline()
for x in f:
    pyautogui.press('tab')
    key_check()
    tokens = x.split(",")
    for i in range(len(tokens)):
        if (i == 0):
            f2.write(tokens[i] + "\n")
            continue
        key_check()
        print(tokens[i])
        if (tokens[i] == "JK"):
            pyautogui.typewrite("Kindergarten")
        elif (i == 26):
            if (int(tokens[i]) < 150):
                pyautogui.typewrite("<150")
            elif (int(tokens[i]) < 300):
                pyautogui.typewrite("150")
            elif (int(tokens[i]) < 600):
                pyautogui.typewrite("300")
            elif (int(tokens[i]) < 1000):
                pyautogui.typewrite("600")
            else:
                pyautogui.typewrite(">1000")
        elif (tokens[i] == "French Immersion"):
            pyautogui.typewrite("Immersion")
        else:
            pyautogui.typewrite(tokens[i])
        #pyautogui.press('enter')
        key_check()
        pyautogui.press('tab')
        key_check()
        time.sleep(0.2)
    time.sleep(0.5)
    key_check()
    pyautogui.press('enter')
    key_check()
    time.sleep(0.5)
    while (True):
        if (keyboard.is_pressed('n')):
            break
    #pyautogui.press('tab')
    #submit
    #pyautogui.press('enter')
    pyautogui.click(1450, 670)
    time.sleep(4)
    pyautogui.press('f5')
    time.sleep(4)
    pyautogui.click(65, 650)
    time.sleep(1)

f.close()
f2.close()