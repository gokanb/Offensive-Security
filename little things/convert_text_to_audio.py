
from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = 'en'
sp = gTTS( text = ' Can you Come Over? ',
          lang= language, slow=False)

sp.save(audio)
playsound(audio)
