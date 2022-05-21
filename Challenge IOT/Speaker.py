# importando pyttsx3
import pyttsx3 as tts


# Método que recebe como parametro a frase que a IA irá dizer
def Speaker(phrase):
    speaker = tts.init()
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate',  rate - 25)
    speaker.setProperty('voice', b'brasil')
    speaker.say(phrase)
    speaker.runAndWait()