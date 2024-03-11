import pyautogui
import webbrowser
import os
import time


# Initial mouse position
initial_position = pyautogui.position()

# Loop until there is mouse movement
while True:
    if pyautogui.position() != initial_position:
        # Open the YouTube link
        webbrowser.open('https://www.youtube.com/watch?v=CK-IzQhc5A8')
        # For Windows, set the volume to max
        if os.name == 'nt':
            os.system('powershell (New-Object -ComObject WScript.Shell).SendKeys((^ 100))')
       
        break
    time.sleep(1)
       
