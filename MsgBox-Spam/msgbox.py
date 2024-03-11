from pynput import keyboard, mouse
import tkinter as tk
import random
import winsound
import threading

# Global variable to indicate if spamming has started
spam_started = False

# Global root Tkinter instance
root = tk.Tk()
root.withdraw()  # Hide the root window

def create_msg_box():
    winsound.MessageBeep()
    window = tk.Toplevel(root)
    window.title("Get fucked")
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
    global spam_started
    if spam_started:
        # Random delay before showing the message box
        root.after(random.randint(1000, 10000), create_msg_box)
        # Schedule the next check
        root.after(random.randint(1000, 10000), msg_popup_randomly)

def on_move(x, y):
    global spam_started
    if not spam_started:
        spam_started = True
        msg_popup_randomly()  # Start spamming message boxes after detecting mouse movement

def listen_for_mouse_movement():
    with mouse.Listener(on_move=on_move) as listener:
        listener.join()

if __name__ == "__main__":
    mouse_thread = threading.Thread(target=listen_for_mouse_movement)
    mouse_thread.start()
    root.mainloop()
