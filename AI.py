import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests


print('Your AI personal assistant is being loaded – CAREN’)

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning Sir/Mam")
        print("Good Morning Sir/Mam")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir/Mam")
        print("Good Afternoon Sir/Mam")
    elif hour>=18 and hour<20:
        speak("Good Evening Sir/Mam")
        print("Good Evening Sir/Mam")
   else:
       speak(“Good Night Sir/Mam)
       print(“Good Night Sir/Mam)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Detecting your words……...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon please, I am not able to understand")
            return "None"
        return statement

speak("Your AI personal assistant is being loaded CAREN")
wishMe()


if __name__=='__main__':


    while True:
        speak("Kindly tell me how can I help you?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "Ok bye" in statement or "stop" in statement or “bye bye” in the statement:
            speak('Hope you enjoyed my service. Your personal assistance CAREN is being shutting down. Bye bye, Takecare')
            print(' Hope you enjoyed my service. Your personal assistance CAREN is being shutting down. Bye bye, Takecare')
            break



        if 'wikipedia' in statement:
            speak('Searching for Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to the Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement or ‘search youtube’ in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("You can see youtube on your window")
            time.sleep(5)

        elif 'open google' in statement or ‘search google’ in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is opened now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Elektra version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Sanyam Dhawan, Aditya Joshi, Taranjeet Singh, Nikhilesh Sharma, and Shivam Kapoor")
            print("I was built by Sanyam Dhawan, Aditya Joshi, Taranjeet Singh, Nikhilesh Sharma, and Shivam Kapoor")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in statement or "sign out" in statement or "sign off" in statement:
            speak("Ok , your pc will log off in 10 seconds make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)
