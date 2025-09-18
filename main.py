import os
import subprocess
from pynput import keyboard
import pytesseract
from PIL import Image
import pyperclip

def capture_screen():
    """
    Captures a selected area of the screen using scrot.
    """
    tmp_file = "/tmp/screenshot.png"
    command = ["scrot", "-s", tmp_file]
    try:
        subprocess.run(command, check=True)
        return tmp_file
    except subprocess.CalledProcessError as e:
        print(f"Error during screen capture: {e}")
        return None
    except FileNotFoundError:
        print("scrot not found. Please make sure it's installed.")
        return None

def recognize_text(image_path):
    """
    Performs OCR on an image file.
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except FileNotFoundError:
        print(f"Image file not found at {image_path}")
        return ""
    except Exception as e:
        print(f"An error occurred during OCR: {e}")
        return ""

def ocr_process():
    """
    The main OCR process.
    """
    image_path = capture_screen()
    if image_path:
        text = recognize_text(image_path)
        if text:
            pyperclip.copy(text)
            print("Text copied to clipboard.")
        os.remove(image_path)

# The key combination to listen for.
COMBINATION = {keyboard.Key.cmd, keyboard.KeyCode.from_char('z')}

# The set of currently pressed keys
current_keys = set()

def on_press(key):
    if key in COMBINATION:
        current_keys.add(key)
        if all(k in current_keys for k in COMBINATION):
            ocr_process()

def on_release(key):
    try:
        current_keys.remove(key)
    except KeyError:
        pass
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
