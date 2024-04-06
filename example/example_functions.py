import pyautogui
import pyscreeze
import cv2
import time

#locates one image on the screen
def test():
    folder = pyautogui.locateOnScreen("images/folder.png", confidence=0.8)
    if folder:
        pyautogui.moveTo(folder)

#locates multiple images on the screen depending on whats in the array
def testMultiple():
    allObjects = ["images/folder.png", "images/bat.png"]
    for i in allObjects:
        i = pyautogui.locateOnScreen(i, confidence=0.8)
        if i:
            pyautogui.moveTo(i)
            #user can decide if they want to break the loop after finding one image.
            break


#test()
#testMultiple()