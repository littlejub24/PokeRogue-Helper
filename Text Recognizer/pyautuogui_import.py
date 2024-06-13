import pyautogui

try: 
    res = pyautogui.locateOnScreen("edit.png")
    print(res)
except pyautogui.ImageNotFoundException:
    print("image not found on screen")