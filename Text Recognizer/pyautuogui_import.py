import pyautogui

try:
    grass = pyautogui.locateOnScreen(r"C:\Users\Zach\Desktop\PokeRouge\PokeRogue-Helper\Text Recognizer\Images\Grass_test.png")
    print(grass)
except pyautogui.ImageNotFoundException:
    print("Image not found on the screen.")
except Exception as e:
    print(f"An error occurred: {e}")