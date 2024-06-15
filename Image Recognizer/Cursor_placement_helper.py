import pyautogui, time, sys, os

def track_cursor_position(duration=5, interval=0.1):
    """
    Track and print the cursor's position for the specified duration.
    
    :param duration: Total time to track the cursor (in seconds).
    :param interval: Interval between position checks (in seconds).
    """
    start_time = time.time()
    while time.time() - start_time < duration:
        x, y = pyautogui.position()
        print(f"Cursor position: ({x}, {y})")
        time.sleep(interval)

track_cursor_position(duration=5, interval=1)