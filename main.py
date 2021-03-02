import clipboard
import pyautogui
import time

pyautogui.alert("Read Instructions Carefully",title="Type Kiddy")
while True:
    all_text = clipboard.paste()
    inp=pyautogui.prompt("Copy text that you want to type then Press OK and place cursur in type area\n "
                         "(OR) "
                         "\n Enter \"Close\"and press OK to stop execution",title="Instructions")
    if inp=="close" or inp=="Close" or inp=="CLOSE":
        break

    time.sleep(4)
    pyautogui.typewrite(all_text)
pyautogui.alert("Thanks for using Type Kiddy. \n Created by @karthifairhawn \n\n To Donate \n G-Pay : +918428988702 \n PhonePay : +918428988702")




