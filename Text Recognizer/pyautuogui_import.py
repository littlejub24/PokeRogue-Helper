import pyautogui

print("hi")

try: 
    res = pyautogui.locateOnScreen('edit.png')
    print(res)
except pyautogui.ImageNotFoundException:
    print("image not found on screen")