import speech_recognition as sr
import time
import keyboard
import threading

u = False

r = sr.Recognizer()

def listenConvertType():
    with sr.Microphone() as source:
        global u
        while(u == True):
            pass
        u = True
        # read the audio data from the default microphone
        audio_data = r.record(source, duration=5)
        #print("Recognizing...")
        u = False
        # convert speech to text
        t = threading.Thread(target=listenConvertType, args=())
        t.start()

        try:
            text = r.recognize_google(audio_data)
        except sr.RequestError:
            text = ''
        except sr.UnknownValueError:
            text = ''
        #print(text)
        keyboard.write(text)
	if(len(text) > 0):
	    keyboard.press('enter')

listenConvertType()
