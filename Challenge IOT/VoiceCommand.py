# importando speech_recognition
import speech_recognition as sr


# Método que ativa o Microfone
def Voice():
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        print('...')
        audio = recon.listen(source)
        audio_pt_br = recon.recognize_google(audio, language="pt-br")
    return audio_pt_br
