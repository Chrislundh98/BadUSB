import tkinter as tk
import random
import time
from pynput import keyboard
import winsound

# Global variable to track if the program should close
should_close = False

# Global root Tkinter instance
root = tk.Tk()
root.withdraw()  # Hide the root window

def create_msg_box():
    winsound.MessageBeep()
    window = tk.Toplevel(root)
    window.title("Get fucked ")
    tk.Label(window, text="haha u is haxckd\n\n call 0769-6942069 for techsupport", font=("Comic Sans", 16)).pack(pady=20)
    tk.Button(window, text="halp plz", command=window.destroy, font=("Comic Sans", 12)).pack(pady=10)

    window_width = 400
    window_height = 200

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = random.randint(0, screen_width - window_width)
    y = random.randint(0, screen_height - window_height)
    window.geometry(f'{window_width}x{window_height}+{x}+{y}')

def msg_popup_randomly():
    if not should_close:
        # Random delay before showing the message box
        root.after(random.randint(1000, 10000), create_msg_box)
        # Schedule the next check
        root.after(random.randint(1000, 10000), msg_popup_randomly)

keys_pressed = set()

def on_press(key):
    global should_close
    keys_pressed.add(key)
    if {keyboard.Key.ctrl_l, keyboard.Key.ctrl_r} <= keys_pressed and not should_close:
        print("Both Ctrl keys pressed - starting countdown")
        # Use 'after' to schedule the check for 5 seconds later
        root.after(5000, check_keys_held)

def check_keys_held():
    if {keyboard.Key.ctrl_l, keyboard.Key.ctrl_r} <= keys_pressed:
        print("Both Ctrl keys held for 5 seconds - closing program")
        global should_close
        should_close = True
        root.quit()  # This will break the mainloop and allow the script to finish

def on_release(key):
    keys_pressed.discard(key)

def listen_for_exit_combo():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

if __name__ == "__main__":
    listen_for_exit_combo()  # Start listening for the exit key combo
    msg_popup_randomly()     # Start showing message boxes at random intervals
    root.mainloop()          # Start the main Tkinter event loop
