import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3
import threading
import time

# Function to update the talk bubble text in chunks
def update_talk_bubble(text, label, sentence_delay=0.55, word_delay=0.3):
    sentences = text.split('. ')
    display_text = ''
    for sentence in sentences:
        words = sentence.split(' ')
        for word in words:
            display_text += word + ' '
            label.config(text=display_text)
            label.update_idletasks()
            time.sleep(word_delay)
        time.sleep(sentence_delay)  # Longer pause at the end of a sentence


# Function to speak the text and update the bubble
def speak_and_update(text, label):
    threading.Thread(target=lambda: update_talk_bubble(text, label)).start()
    engine.say(text)
    engine.runAndWait()

# Initialize the speech engine
engine = pyttsx3.init()
voice = engine.getProperty('voices')[1]
engine.setProperty('voice', voice.id)
engine.setProperty('pitch', 70)

# Tkinter setup
root = tk.Tk()
root.title("Alien Message")

# Load and resize the image
image_path = "c:\\Users\\Christoffer Lundh\\OneDrive - Jonkoping University\\Documents\\alien\\alientux.png"  # Updated to the new file location
original_image = Image.open(image_path)
resized_image = original_image.resize((200, 200))  # Resize to 200x200 pixels
photo = ImageTk.PhotoImage(resized_image)

# Display the image
image_label = tk.Label(root, image=photo)
image_label.pack()

# Display the talk bubble as a label
talk_bubble = tk.Label(root, text="", wraplength=180, justify='left', bg='lightgrey', fg='black')
talk_bubble.pack(pady=10)

# The alien message
alien_message = ('Greetings to the inhabitants of planet Earth. I am an alien from a distant planet named Hak5 '
                 'and I have taken control of this computer to communicate with you. I want to announce to you '
                 'that in exactly one year\'s time our invasion fleet will arrive on your planet because we have '
                 'heard that you make very good fries. Resistance is useless. Your only option is to give us all '
                 'the fries you have and to produce as many as possible to satiate us. Your planet will become a '
                 'potato chip colony and you will produce forever. Get ready, earthlings. Our hunger is near.')

# Start the speech and bubble update in a separate thread to keep the GUI responsive
threading.Thread(target=lambda: speak_and_update(alien_message, talk_bubble)).start()

root.mainloop()
