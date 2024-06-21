try: 
    res = pyautogui.locateOnScreen('edit.png', grayscale=True,confidence=0.9)
    print(res)
except pyautogui.ImageNotFoundException:
    print("image not found on screen")