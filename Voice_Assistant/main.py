import speech_recognition as sr
import pyttsx3 as p
from pyaudio import *
import datetime
import os
import pyjokes
import webbrowser
import selenium.webdriver as sel

#Initiation

engine = p.init()
r = sr.Recognizer()
driver = sel.Chrome("C:\Program Files\Google\Chrome\Application\chrome.exe")


#Female Voice

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#Rate

rate = engine.getProperty('rate')
engine.setProperty('rate',150)

#to speak

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#ask name

def askname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome " + uname)

# Welcome voice
        
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")   
  
    else:
        speak("Good Evening Sir !")  
  
    assname =("zuzii 3 point o were created by sivanesh")
    speak("I am your Assistant")
    speak(assname)

#take command

def takeCommand():
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)    
        speak("Unable to Recognize your voice.")  
        return 'none'
     
    return query





if __name__ == '__main__':
    clear = lambda: os.system('cls')


    wishMe()
    askname()


    while True:
         
        query = takeCommand().lower()


        if "who are you" in query:
            speak("I am your virtual assistant created by Mister sivanesh")
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister sivanesh")


        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
 
        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Sivanesh.")


        elif "how are you"  in query:
            speak('I am good, Thanks for caring')

        elif 'your' and 'name' in query :
            speak("zuzii 3 point o were created by sivanesh")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "who i am" in query:
            speak("If you talk then definitely your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to sivanesh. further It's a secret")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
        
        elif "will you be my gf" in query or "will you be my bf" in query:   
            speak("I'm not sure about, may be you should give me some time")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
        
        elif 'search' or 'what' or 'what is' or "who is" "how to" or 'how' in query:
            
            driver.get('www.google.com')
        #     driver.find_element(by=id,'')
                    
        elif 'google.com' in query or 'google' in query:
                     
            driver.get("www.google.com")


        elif "wikipedia" in query:
            
            driver.get("www.wikipedia.com")

        

        
            