import pyautogui

try: 
    res = pyautogui.locateOnScreen(r"C:\Users\Zach\Desktop\PokeRouge\PokeRogue-Helper\Text Recognizer\Images\edit.png")
    print(res)
except pyautogui.ImageNotFoundException:
    print("image not found on screen")
    