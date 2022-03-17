import gtts
from playsound import playsound

tts = gtts.gTTS("Hola mundo", lang="es")

tts.save("hello_spanish.mp3")

playsound("hello_spanish.mp3")
