import pyautogui, time, sys, os

def find_matching_image(folder_path, region=None, confidence=0.7):
    """
    Iterate through images in the folder and return the first image that matches the screen.
    
    :param folder_path: Path to the folder containing the images.
    :param region: (optional) Region (x, y, width, height) to search within.
    :param confidence: (optional) Confidence level for image matching.
    :return: Name of the matching image file, or None if no match is found.
    """
    for image_name in os.listdir(folder_path):
        if image_name.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, image_name)
            print(f"Searching for {image_path} in region {region} with confidence {confidence}...")
            try:
                match = pyautogui.locateOnScreen(image_path, region=region, confidence=confidence)
                if match:
                    return image_name
            except pyautogui.ImageNotFoundException:
                print(f"Image not found: {image_name}")
                continue  # Continue to the next image if not found
            except Exception as e:
                print(f"An error occurred: {e}")
                continue  # Continue to the next image if any other error occurs
    return None
# Calculate the region based on given cursor positions
top_left = (184, 221)
top_right = (1126, 223)
bottom_left = (199, 493)
bottom_right = (924, 546)

x = min(top_left[0], bottom_left[0])
y = min(top_left[1], top_right[1])
width = max(top_right[0], bottom_right[0]) - x
height = max(bottom_left[1], bottom_right[1]) - y

region = (x, y, width, height)

# Specify the folder path containing your images
folder_path = r'C:\Users\Zach\Desktop\PokeRouge\PokeRogue-Helper\Image Recognizer\Images\SoloTypes'

# Find the matching image in the specified region
matching_image = find_matching_image(folder_path, region=region, confidence=0.7)

if matching_image:
    print(f"Found a matching image: {matching_image}")
else:
    print("No matching image found.")