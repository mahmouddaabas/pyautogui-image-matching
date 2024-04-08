# use this to take screenshots by pressing X

import pyautogui
import keyboard

counter = 0

print('Press X to take a screenshot of the screen.')
while True:
    if keyboard.is_pressed('x'):
        image = pyautogui.screenshot('images/uncut/screenshot'+str(counter)+'.png')
        counter += 1
