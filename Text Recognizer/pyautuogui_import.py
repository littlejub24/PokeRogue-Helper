import pyautogui

try:
    grass = pyautogui.locateOnScreen(r"C:\Users\Zach\Desktop\PokeRouge\PokeRogue-Helper\Text Recognizer\Images\shape_10.jpg")
    print (grass)
except pyautogui.ImageNotFoundException:
    print("image not found on screen")
    