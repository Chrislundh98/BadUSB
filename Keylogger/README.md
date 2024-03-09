# Educational Keylogger for Windows
> **Disclaimer**: This project is strictly for educational purposes only. The developer assumes no responsibility for any malicious use of the files in this repository.

## Developed by Chris

## Description
This repository is designed for educational exploration of cybersecurity concepts using FlipperZero/BadUSB. It includes DuckyScripts, PowerShell commands, Base64 encoding/decoding, Python scripts, and utilizes Discord for reporting. The script functions as a keylogger, recording keystrokes to `key_logs.txt` and sending this file's content to a specified Discord server every minute. **Note**: This keylogger is tailored for Windows devices only.

## Setup Instructions
1. **Discord Server Setup**
   - Create a private Discord server.
   - Add a text channel and configure a webhook.

2. **Repository Setup**
   - Fork or create a new GitHub repository.
   - Modify `keylogger.py` to utilize your Discord webhook URL.
   - Compile `keylogger.py` to `keylogger.exe`, encode it using a Base64 encoder, and upload the encoded file to your repository.
   - Navigate to the encoded file, click "RAW", and copy the URL.

3. **FlipperZero/BadUSB Preparation**
   - Replace the URL in `keylog_encoded.txt` with the one from step 2 and replace all mentions of `.txt` with your encoded file.
   - Use qFlipper or any file management tool to upload `keylog_encoded.txt` to your BadUSB device.

## To-Do List
- [ ] Create and configure a Discord server.
- [ ] Set up a GitHub repository.
- [ ] Adjust the keylogger script for your use case.
- [ ] Compile, encode, and upload your custom keylogger.
- [ ] Deploy the script to a BadUSB device.

_Happy Hacking! Remember to use this tool responsibly and ethically._

