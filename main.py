import time
import keyboard
from datetime import datetime
from pynput import keyboard as something

# Hides the CommandPrompt after starting the Script
'''
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)
'''

# Creates the Keyboard
kb = something.Controller()
button_to_move = 'r'


# presses a Button for x Seconds
def make_r(time_sec):
    now = int(datetime.now().strftime("%H%M%S"))
    later = now + time_sec
    while later > int(datetime.now().strftime("%H%M%S")):
        time.sleep(0.001)
        kb.press(button_to_move)
        time.sleep(0.1)
        check_for_map_open()
    kb.release(button_to_move)


def check_for_map_open():
    if keyboard.is_pressed('m'):
        kb.release(button_to_move)
        time.sleep(10)
        i = 0
        while i != 5:
            i += 1
            kb.press('e')
            kb.release('e')
            time.sleep(0.2)
            kb.press('q')
            kb.release('q')


# Concrete Script to loop the Combo
while True:
    check_for_map_open()
    a = 0
    time.sleep(0.2)
    kb.press('q')
    kb.release('q')
    while a <= 20:
        check_for_map_open()
        make_r(4)
        a = a + 4
        time.sleep(0.2)
        kb.press('e')
        kb.release('e')
