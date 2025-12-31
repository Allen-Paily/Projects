# The goal is to grind xp in black myth wukong. 
# Issues- every 40-ish cycles the destined one goes off the trail and loses his path. 
# get ~2000 will each cycle
import time
import pyautogui 

time.sleep(2) # Insert time just to tab into application.

def up(x):
    pyautogui.keyDown('w')
    time.sleep(x) # Insert time
    pyautogui.keyUp('w')

def down(x):
    pyautogui.keyDown('s')
    time.sleep(x) # Insert time
    pyautogui.keyUp('s')

def left(x):
    pyautogui.keyDown('a')
    time.sleep(x) # Insert time
    pyautogui.keyUp('a')    

def right(x):
    pyautogui.keyDown('d')
    time.sleep(x) # Insert time
    pyautogui.keyUp('d')

def shrine():
    pyautogui.press('e')
    time.sleep(4.5)
    pyautogui.press('e')
    time.sleep(4)
    pyautogui.press('escape')

#everything in the for loop is counted as one cycle
for i in range(100):
    time.sleep(1)
    down(1.5)
    right(5)
    with pyautogui.hold('d'):
        up(5.9)
    up(1.8)
    pyautogui.press('4')
    time.sleep(2)
    pyautogui.press('4')
    time.sleep(4)
    down(2.3)
    with pyautogui.hold('a'):
        down(5.9)
    left(4.4)
    up(1.3)
    shrine()
    print(i)
    time.sleep(4)