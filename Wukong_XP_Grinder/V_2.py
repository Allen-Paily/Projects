# The goal is to grind xp in black myth wukong. 
# Now uses the talisman to teleport back to the shrine
#issues - only get ~800-900 will instead of the usual ~2000 because of the use of the talisman
# good for when you dont care about will grinding 
import time
import pyautogui 

time.sleep(2) # Insert time

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
    time.sleep(3.8)
    pyautogui.press('escape')


for i in range(1000):
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
    pyautogui.press('q')
    time.sleep(13)
    if (i%5==0):
        time.sleep(5)
        shrine()
    print(i)