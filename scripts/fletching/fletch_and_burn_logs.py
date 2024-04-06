import pyautogui
import cv2
import time
import os
import sys

# Get the directory of the script
script_dir = os.path.dirname(__file__)

def adjustCamera():
    pyautogui.moveTo(260, 142)
    time.sleep(1)
    pyautogui.scroll(-2000)

def openBank():
    bank_image_path = os.path.join(script_dir, "images", "Bank.png")
    bank = pyautogui.locateOnScreen(bank_image_path, confidence=0.6)
    if bank:
        print('Opening bank.')
        image_center = pyautogui.center(bank)
        pyautogui.moveTo(image_center)
        pyautogui.click()

def getLogsFromBank():
    logs_image_path = os.path.join(script_dir, "images", "BloodLogs.png")
    logs = pyautogui.locateOnScreen(logs_image_path, confidence=0.7)
    if logs:
        image_center = pyautogui.center(logs)
        pyautogui.moveTo(image_center)
        pyautogui.click(button='right')
        withdrawLogs_image_path = os.path.join(script_dir, "images", "WithdrawAllLogs.png")
        withdrawLogs = pyautogui.locateOnScreen(withdrawLogs_image_path, confidence=0.9)
        if withdrawLogs:
            print('Taking out blood logs.')
            image_center = pyautogui.center(withdrawLogs)
            pyautogui.moveTo(image_center)
            pyautogui.click()
            time.sleep(1)
            # close bank
            pyautogui.moveTo(486, 55)
            pyautogui.click()

def fletchLogs():
    fletchingKnife_image_path = os.path.join(script_dir, "images", "FletchingKnife.png")
    fletchingKnife = pyautogui.locateOnScreen(fletchingKnife_image_path, confidence=0.7)
    if fletchingKnife:
        image_center = pyautogui.center(fletchingKnife)
        pyautogui.moveTo(image_center)
        pyautogui.click()
        logs_image_path = os.path.join(script_dir, "images", "BloodLogs.png")
        logs = pyautogui.locateOnScreen(logs_image_path, confidence=0.7)
        if logs:
            print('Fletching logs.')
            image_center = pyautogui.center(logs)
            pyautogui.moveTo(image_center)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(263, 444)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(2)
            pyautogui.moveTo(256, 507)
            time.sleep(2)
            pyautogui.click()
            time.sleep(2)
            pyautogui.write('100')
            time.sleep(2)
            pyautogui.press('enter')

def burnKindlings():
    kindling_image_path = os.path.join(script_dir, "images", "BloodKindling.png")
    kindling = pyautogui.locateOnScreen(kindling_image_path, confidence=0.8)
    if kindling:
        image_center = pyautogui.center(kindling)
        pyautogui.moveTo(image_center)
        pyautogui.click()
        bloodFurnace_image_path = os.path.join(script_dir, "images", "BloodFurnace.png")
        bloodFurnace = pyautogui.locateOnScreen(bloodFurnace_image_path, confidence=0.8, region=(0, 0, 513, 337))
        if bloodFurnace:
            print('Burning logs.')
            image_center = pyautogui.center(bloodFurnace)
            pyautogui.moveTo(image_center)
            pyautogui.click()
            time.sleep(3)
            pyautogui.moveTo(273, 229)
            time.sleep(3)
            pyautogui.click()
            time.sleep(3)
            pyautogui.moveTo(263, 444)
            time.sleep(1)
            pyautogui.click(button='right')
            time.sleep(2)
            pyautogui.moveTo(256, 507)
            time.sleep(2)
            pyautogui.click()

def main():
    print('Fletching script will start in 5 seconds.')
    time.sleep(5)
    adjustCamera()
    while True:
        try:
            time.sleep(2)
            openBank()
            time.sleep(3)
            getLogsFromBank()
            time.sleep(3)
            fletchLogs()
            time.sleep(50)
            burnKindlings()
            time.sleep(50)
        except KeyboardInterrupt:
            print('CTRL+ C detected, exiting script.')
            sys.exit(0)
        except Exception as e:
            print('Error, retrying...')
        