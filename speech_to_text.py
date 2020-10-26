import speech_recognition as s
sr = s.Recognizer()
mic = s.Microphone()
with mic as source:
    sr.adjust_for_ambient_noise(source)
    print("I am listening you...")
    audio = sr.listen(source,timeout = 10)
    print(sr.recognize_google(audio,language ='en-IN'))
