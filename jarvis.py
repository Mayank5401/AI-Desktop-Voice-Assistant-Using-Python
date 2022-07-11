
import datetime
import smtplib
import pyttsx3
import pyaudio 
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12 :
        print("Good Morning!")  
    elif hour>=12 and hour<18:
        print("Good Afternoon!")
    else :
        print("Good Evening!")

    speak("Jarvis here . How can I help You Sir?")
    
def takeCommand():
    #takes microphone input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising......")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
        
    except Exception as e:
        print("Say that again please.......")
        return "None"
    return query   
    
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mayankp.ip.19@nitj.ac.in','your_password')
    server.sendmail('mayankp.ip.19@nitj.ac.in',to,content)
    server.close()


if __name__=="__main__" :
    wishMe()   
    if True:
         query=takeCommand().lower()

         if 'wikipedia' in query:
             speak('Searching Wikipedia.....')
             query=query.replace("wikipedia","")
             results=wikipedia.summary(query,sentences=2)
             speak("According to Wikipedia")
             print(results)
             speak(results)

         elif 'open youtube' in query:
             speak('Opening You Tube......')
             webbrowser.open("youtube.com")  

         elif 'open google' in query:
             speak('Opening Google.......')
             webbrowser.open("google.com")

         elif 'open stackoverflow' in query:
             speak('Opening Stack Overflow.......')
             webbrowser.open("stackoverflow.com") 
        
         elif 'play music' in query:
             speak('Playing Music.......')
             music_dir='C:\\Users\\Mayank\\Downloads\\Music'
             songs=os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir,songs[0]))

         elif 'the time' in query:
             strTime=datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Sir ,the time is {strTime}")
         
         elif 'open code' in query:
              codePath='C:\\Users\\Mayank\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
              os.startfile(codePath)
        
         elif 'email to mayank' in query:
              try:
                  speak("What shoud I say?")
                  content=takeCommand()
                  to="mayankp.ip.19@nitj.ac.in"
                  sendEmail(to,content)
                  speak("Email has been sent!")

              except Exception as e:
                   print(e)
                   speak("Sorry Sir. I am not able to send this email.")

