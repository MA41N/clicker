import keyboard
import mouse
import time

isClicking = False

def set_isClicker():
    global isClicking
    if isClicking:
        isClicking = False
        print("Кликер отключен")
    else:
        isClicking = True
        print("Кликер включен")

keyboard.add_hotkey('; + ]', set_isClicker)

while True:
    if isClicking:
        mouse.double_click(button='left')
        time.sleep(0.01)