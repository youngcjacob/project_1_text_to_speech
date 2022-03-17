# still receiving issues on this one. Objective is to play the audio without needing to save an mp3 file
from gtts import gTTS
import gtts
from playsound import playsound
from io import BytesIO


mp3_fp = BytesIO()
tts = gtts.gTTS("This is fun", lang='en')
tts.write_to_fp(mp3_fp)

mp3_fp = BytesIO()
tts = gTTS('hello', lang='en')
tts.write_to_fp(mp3_fp)
