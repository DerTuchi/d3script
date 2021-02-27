import time
import keyboard
from datetime import datetime
from pynput import keyboard as something

# Hides the CommandPrompt after starting the Script
'''
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)
'''

# Config:
strafe = 'r'
vengeance = 'q'
hungering_arrow = 'e'
companion = 'w'
open_map = 'm'

# Creates the Keyboard
kb = something.Controller()


# presses a Button for x Seconds
def make_strafe(time_sec):
    now = int(datetime.now().strftime("%H%M%S"))
    later = now + time_sec
    while later > int(datetime.now().strftime("%H%M%S")):
        time.sleep(0.001)
        kb.press(strafe)
        time.sleep(0.1)
        check_for_map_open()
    kb.release(strafe)

#stops the script if Map was opened
def check_for_map_open():
    if keyboard.is_pressed(open_map):
        kb.release(strafe)
        time.sleep(10)
        i = 0
        while i != 5:
            i += 1
            kb.press(hungering_arrow)
            kb.release(hungering_arrow)
            time.sleep(0.2)
            kb.press(vengeance)
            kb.release(vengeance)


# Concrete Script to loop the Combo
while True:
    check_for_map_open()
    a = 0
    time.sleep(0.2)
    kb.press(vengeance)
    kb.release(vengeance)
    kb.press(companion)
    kb.release(companion)
    while a <= 20:
        check_for_map_open()
        make_strafe(4)
        a = a + 4
        time.sleep(0.2)
        kb.press(hungering_arrow)
        kb.release(hungering_arrow)
