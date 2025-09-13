from pynput.mouse import Controller as MouseController
from pynput.mouse import Controller as MouseController, Button
import pyautogui
import keyboard
import time

mouse = MouseController()
mousepos = mouse.position

def enter():
    keyboard.press('enter')

mouse.position = (1615, 1423)
mouse.click(Button.left)
time.sleep(0.4)
mouse.position = (1081, 1318)
mouse.click(Button.left)

def meme():
    mouse.position = (1081, 1318)
    mouse.click(Button.right)
    mouse.position = (1151, 1335)
    mouse.position = (1150, 1334)
    mouse.click(Button.left, 2)
    time.sleep(0.009)
    mouse.click(Button.left, 2)
    enter()

for i in range(20):
    time.sleep(1)
    meme()
