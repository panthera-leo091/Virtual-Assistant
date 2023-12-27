from cProfile import label
from turtle import goto
from itertools import count
import pyttsx3
import datetime
import pywhatkit
import speech_recognition as sr
import wikipedia
import webbrowser


"""
cProfile
itertools
turtel
pyttsx3
datetime
pywhatkit
speech_recognition
wikipedia
webbrowser
"""

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

'''
# print(voices[0].id)
# print(voices[1].id)
# print(voices[2].id)
# print(voices[3].id)
# print(voices[4].id)
# print(voices[5].id)

# """
# voice[0] = HAZEL_11.0     #preinstalled
# voice[1] = HazelM
# voice[2] = HeeraM
# voice[3] = RaviM(man)
# voice[4] = GeorgeM(man)
# voice[5] = ZIRA_11.0      #preinstalled
# """
'''

engine.setProperty('voice', voices[1].id)


def speak(audio):
    # every time we pass speak command it take an argument to and use to speak the given aurgument
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """
    this will be the first word when command Jarvice is turm on
    it first check time and great the user
    """

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('good morning')
    elif hour > 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    # speak("welcome sir")
    speak("I am your first Virtual Assistant. AWANI.")
    print('What can i do for you')
    speak('what can i do for you')


def takecommand():
    """
    take microphone input from user
    and returm string
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("user said:", query)
    except Exception as e:
        print(e)
        print("can't recognize you. try again")
        return "None"
    return query

if __name__ == "__main__":
    # speak("Welcome Sir")
    
    wishMe()
    count = 0
    while True:
        query = takecommand().lower()
        
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stakeoverflow' in query:
            webbrowser.open("stakeoverflow.com")

        # elif 'play music' in query:
        #     music_dir = ''

        elif 'the date' in query:
            strDate = datetime.datetime.now().date
            speak(f"Sir, the Date is {strDate}")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "what can you do" in query:
            print('I can search wikipedia, open youtube and browsers, and many more')
            speak('I can search wikipedia, open youtube and browsers, and many more')

        elif "good night" in query:
            h = datetime.datetime.now().hour
            if h in range(0, 5):
                print("It's too late \nGood Night and Sweet Dream's Sir...")
                speak("It's too late Good Night and Sweet Dream's Sir...")
            else:
                print("Good Night and Sweet Dream's Sir...")
                speak("Good Night and Sweet Dream's Sir...")
            break

        elif "send message" in query:
            print("who do you want to send message")
            speak("who do you want to send message")
            d1 = {"avanish": "9125211006", "ashish": "8957864900", "ayush": "6306154825", "utkarsh": "7522084614", "papa": "8127552220"}
            label .takecmnd
            query1 = takecommand().lower()
            if query1 in d1:
                print("what's the message")
                speak("what's the message")
                query2 = takecommand().lower()
                hour = int(datetime.datetime.now().hour)
                min = int(datetime.datetime.now().minute)
                min += 1
                pywhatkit.sendwhatmsg(d1[query1], query2, hour, min)
                print("sending", query2, "to", query1, "in less then 2 min")
            else:
                print("can't find contact please speak again")
                speak("can't find contact please speak again")
                goto .takecmnd

        # elif "reminder"
        
        
        else:
            count += 1
            if count == 2:
                break
            else:
                continue