import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import pywhatkit
import wikipedia
import pyautogui
import keyboard
import cv2
import numpy as np
import time
import HandTrackingModule as htm
from playsound import playsound
from googletrans import Translator


####################################



####################################



assistant=pyttsx3.init('sapi5')
voices=assistant.getProperty('voices')

assistant.setProperty(('voice'), voices[8].id)
assistant.setProperty('rate', 170)

##THIS IS AUDIO FUNCTION
def speak(audio):
    print(" ")
    assistant.say(audio)
    print(f": {audio}")
    print(" ")
    assistant.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    min = int(datetime.datetime.now().minute)
    if hour>=0 and hour<12:
        speak("good morning sir")
        speak("the time is")
        speak(hour)
        speak(min)
        speak("its a bright sunny day sir get up!")
        
       

    elif hour>=12 and hour<18:
        speak("good afternoon sir ")
        speak("the time is")
        speak(hour)
        speak(min)
        speak("i m feeling sleepy sir i hope you are also feeling that")

       
       
    
    else:
        speak("good evening sir")
        speak("the time is:")
        speak(hour)
        speak(min)
        speak("did you have dinner sir?")
        speak("I m feeling sleepy sir !")
        speak("i m going to sleep sir !")
        speak("sleep tight")
        speak("good night sir")
        speak("sweet dreams")

def takeCommand():
    ##takes microphone input from the user and return string output
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        command.pause_threshold = 1
        
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio,language = 'en-in')
            print(f"you said: {query}")

        except Exception as Error:
                return "none"
            

        return  query.lower()

def taskExe():
    speak('what you want me to do sir?')

    while True:

        query=takeCommand()

        if 'intro' in query:
            intro()
        
        elif 'how are you' in query:
            speak('i am fine sir!')
            speak('what about you?')

        elif 'you need a break' in query:
            speak("OK sir, you can call me anytime")
            break
        
        elif 'bye' in query:
            speak("ok sir bye!")
            break
        elif 'youtube search' in query:
            youtubeSearch()


        elif 'google search' in query:
           googleSearch()



        elif 'launch website' in query:
           websiteLaunch()

        elif 'play music' in query:
            playMusic()

        elif 'wikipedia' in query:
           searchWikipedia()
            

        elif 'whatsapp message' in query:
            whatsapp()
        

        elif 'screenshot' in query:
            screenshot()
        
        elif 'open app' in query:
            openApps()

        elif 'close app' in query:
            closeApp()
         
        elif 'wish me' in query:
            wishMe()
        
        elif 'commands' in query:
           keyboardCommands()

        elif 'turn on the camera' in query:
            openCamera()
      
        elif 'alarm' in query:
            setAlarm()
        
        # elif 'translator' in query:
        #     trans()
        
        elif 'remember that' in query:

            rememberMsg = query.replace("remember","")    
            rememberMsg = rememberMsg.replace("cortana","")
            speak("You tell me to remind you that :" + rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()


        elif 'what do you remember' in query:
            rember = open('data.txt','r')
            speak("You told me to remeber that" + rember.read())
        
        elif 'thanks' in query:
            speak("It's my pleasure sir!")
def whatsapp():
    speak("Tell me the name of the person!")
    name = takeCommand()

    if'harsh' in name:
        speak("Tell me the message sir!")
        msg = takeCommand()
        speak("tell me the time sir!")
        speak("time in hour!")
        hours = int(takeCommand())
        speak("time in minutes")
        minutes = int(takeCommand())
        speak("tell me the phone number sir?")
        pywhatkit.sendwhatmsg("+919013947295", msg, hours ,minutes)
        speak("OK sir , sending the whatsapp mesage !")


    else: 
        ##error in int typecasting for phone no sovle it later
        speak("tell me the phone number sir?")
        phone = (takeCommand())
        ph =  '+91' + phone
        speak("Tell me the message sir!")
        msg = takeCommand()
        speak("tell me the time sir!")
        speak("time in hour!")
        hours = int(takeCommand())
        speak("time in minutes")
        minutes = int(takeCommand())
        speak("tell me the phone number sir?")
        pywhatkit.sendwhatmsg(ph, msg, hours ,minutes)
        speak("OK sir , sending the whatsapp mesage !")

def screenshot():

    speak("OK sir , what should i name that file?")
    path = takeCommand()
    path1name = path + ".png"
    path1 = "D:\\projects\\jarvis ss\\" + path1name
    ss = pyautogui.screenshot()
    ss.save(path1)
    os.startfile("D:\projects\jarvis ss")
    speak("Here is your screenshot sir!")
 
def openApps():
    speak("which app do you want to open sir?")
    q = takeCommand()
    speak("Ok sir , wait a second!")

    if 'vs code' in q:
        os.startfile("C:\\Users\\bhard\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif 'brave browser' in q:
        os.startfile("C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe")

def closeApp():
    speak("which app you want to close sir?")
    v = takeCommand()
    speak("wait a second sir!")

    if 'vs code' in v:
        os.system("TASKKILL /F /im Code.exe")

    elif 'brave browser' in v:
         os.system("TASKKILL /F /im brave.exe")

def intro():
    speak("hello sir, i am cortana")
    speak("your personal ai assistant")
   
    speak("how may i help you")

def youtubeSearch():
     speak('ok sir , this is what i found for your search')
     query = query.replace("jarvis","")
     query = query.replace("youtube search", "")
     web = 'https://www.youtube.com/results?search_query=' + query
     webbrowser.open(web)
     speak('Done sir!')

    

def googleSearch():
     speak('ok sir , this is what i found for your search')
     query = query.replace("jarvis","")
     query = query.replace("google search", "")
     pywhatkit.search(query)
     speak("Done sir!")

def websiteLaunch():
     speak("tell me the name of the website!")
     name = takeCommand()
     web = 'https://www.' + name + '.com'
     webbrowser.open(web)
     speak("Launched...")

def playMusic():
     speak("tell me the name of the song!")
     musicName = takeCommand()
     pywhatkit.playonyt(musicName)
     
def takeHindi():

     ##takes microphone input from the user and return string output
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        command.pause_threshold = 1
        
        audio = command.listen(source)

        try:
            print("Recognizing....")
            query = command.recognize_google(audio,language = 'hi')
            print(f"you said: {query}")

        except Exception as Error:
                return "none"
            

        return  query.lower()


# def trans():     

#     speak("Tell me the word!")
#     line = takeHindi()
#     t = Translator()
#     result = t.translate(line)
#     Text = result.text
#     speak(Text)

            
  
def searchWikipedia():
     speak("Searching wikipedia...")
     query = query.replace("wikipedia","")
     wiki = wikipedia.summary(query,2)
     speak(f"According to wikipedia: {wiki}")

def keyboardCommands():
     speak("whats your command sir?")
     comm = takeCommand()
     

     if 'stop' in comm:
       keyboard.press('space bar')
        
     elif 'play' in comm:
         keyboard.press('space bar')

     elif 'restart' in comm:
         keyboard.press('0')
     elif 'mute' in comm:
          keyboard.press('m')
        
     elif 'skip' in comm:
         keboard.press('l')

     elif 'back' in comm:
      keyboard.press('j')

    
def openCamera():

    ##error camera is not showing only flash is showing
   speak("ok sir turning on the camera , wait a seconed!")
   wCam ,hCam = 640 , 480



   cap = cv2.VideoCapture(0)
   cap.set(3, wCam)
   cap.set(4, hCam)



   while True:
    success , img = cap.read()


   cv2.imshow("Image", img)
   cv2.waitKey(1)

def setAlarm():

            speak("Enter the time!")
            time = input(":enter the time:")

            while True:
                time_at = datetime.datetime.now()
                now = time_at.strftime("%H:%M:%S")


                if now == time:
                    speak("time to wake up sir!")
                    playsound('ringtone.mp3')
                    speak("Alarm Closed!")

                elif now > time:
                    break


speak("hello sir")
speak("tell me what can i do for you?")
order = takeCommand()


if 'listen' in order:
    taskExe()
    