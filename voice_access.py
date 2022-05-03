import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

# speaks out the passed parameter
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def voice_recognizer():
 # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Say something!")
        audio = r.listen(source)

     # recognize speech using google
    try:
        return (r.recognize_google(audio))
    except:
        return ("Error")
