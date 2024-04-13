import pyautogui
import cv2
import time
import os
import sys
import keyboard

counter = 0

def adjustCameraZoomOut():
    print('Zooming out.')
    pyautogui.moveTo(260, 142)
    time.sleep(1)
    pyautogui.scroll(-5000)

def adjustCameraZoomIn():
    print('Zooming in.')
    pyautogui.moveTo(260, 142)
    time.sleep(1)
    pyautogui.scroll(5000)

def adjustCameraDown():
     print('Moving camera down.')
     pyautogui.moveTo(260, 142)
     time.sleep(1)
     for _ in range(15):
        keyboard.press('down')
        time.sleep(0.1)
        keyboard.release('down')
        time.sleep(0.1)

def adjustCameraUp():
     print('Moving camera up.')
     pyautogui.moveTo(260, 142)
     time.sleep(1)
     for _ in range(15):
          keyboard.press('up')
          time.sleep(0.1)
          keyboard.release('up')
          time.sleep(0.1)

def enterLobbyDoor():
    print('Entering lobby door.')
    pyautogui.moveTo(381, 201)
    pyautogui.sleep(1)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(265, 427)
    pyautogui.sleep(1)
    pyautogui.click()

def enterFirstBossDoor():
     print('Entering first boss room.')
     adjustCameraZoomIn()
     time.sleep(3)
     pyautogui.moveTo(458, 184)
     time.sleep(1)
     pyautogui.click()
     time.sleep(3)
     adjustCameraZoomOut()

def attackFirstBoss():
     print('Attacking first boss.')
     pyautogui.moveTo(400, 119)
     time.sleep(1)
     pyautogui.click()
     time.sleep(20)

def enterSecondBossDoor():
     print('Entering second boss room.')
     pyautogui.moveTo(265, 87)
     time.sleep(1)
     pyautogui.click()
     time.sleep(3)

def attackSecondBoss():
     print('Attacking second boss.')
     pyautogui.moveTo(244, 35)
     time.sleep(1)
     pyautogui.click()
     time.sleep(20)

def swapWeapon():
    print('Switching weapon.')
    pyautogui.moveTo(582, 254)
    time.sleep(1)
    pyautogui.click()
    time.sleep(3)

def enterThirdBossDoor():
     print('Entering third boss room.')
     swapWeapon()
     time.sleep(2)
     pyautogui.moveTo(259, 80)
     time.sleep(1)
     pyautogui.click()
     time.sleep(3)

def attackThirdBoss():
     print('Attacking third boss.')
     pyautogui.moveTo(255, 61)
     time.sleep(1)
     pyautogui.click()
     time.sleep(30)

def enterFourthBossDoor():
     print('Entering fourth boss room.')
     adjustCameraDown()
     time.sleep(5)
     pyautogui.moveTo(278, 256)
     time.sleep(1)
     pyautogui.click()
     adjustCameraUp()
     time.sleep(6)

def attackFourthBoss():
     print('Attacking fourth boss.')
     pyautogui.moveTo(191, 342)
     time.sleep(1)
     pyautogui.click()
     time.sleep(30)

def lootChest():
     swapWeapon()
     time.sleep(2)
     print('Looting chest.')
     pyautogui.moveTo(263, 50)
     time.sleep(1)
     pyautogui.click()
     time.sleep(5)
     pyautogui.moveTo(270, 84)
     time.sleep(1)
     pyautogui.click()
     time.sleep(3)

def resetNirv():
     global counter
     if counter >= 10:
          pyautogui.type("::nirv")
          time.sleep(2)
          pyautogui.press('enter')

def main():
    global counter
    print('Running nirvana bot in 5 seconds.')
    time.sleep(2)
    adjustCameraZoomOut()
    time.sleep(2)
    while True:
        resetNirv()
        time.sleep(10)
        enterLobbyDoor()
        time.sleep(3)
        enterFirstBossDoor()
        time.sleep(3)
        attackFirstBoss()
        time.sleep(3)
        enterSecondBossDoor()
        time.sleep(3)
        attackSecondBoss()
        time.sleep(3)
        enterThirdBossDoor()
        time.sleep(3)
        attackThirdBoss()
        time.sleep(3)
        enterFourthBossDoor()
        time.sleep(3)
        attackFourthBoss()
        time.sleep(3)
        lootChest()
        time.sleep(3)
        counter+=1
        print('The bot has completed: ' + str(counter) + " nirvana runs.")

main()

