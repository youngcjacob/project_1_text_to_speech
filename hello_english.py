import gtts
from playsound import playsound
import os

# makes request to google to get the synthesis
tts = gtts.gTTS("Hello World")

# save the audio file
tts.save("hello.mp3")

# play the sound in the audio file
playsound("hello.mp3")

os.remove("hello.mp3")
