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

##for volume control

import cv2
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np


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
        speak("i m feeling sleepy sir , i hope you are also feeling that")

       
       
    
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
    speak('which task you , want to perform sir?')

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

        elif 'volume control' in query:
            speak("wait a second sir!")
            volumeControl()

        elif "change voice" in  query:
            speak("for female say female and , for man say men")
            w = takeCommand()
            
            if "female" in w:
                voiceChange(8)
            elif "men" in w:
                voiceChange(1)

        elif "shutdown" in query:
            shutDown()


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

def volumeControl():

    

 
  cap = cv2.VideoCapture(0) #Checks for camera
 
  mpHands = mp.solutions.hands #detects hand/finger
  hands = mpHands.Hands()   #complete the initialization configuration of hands
  mpDraw = mp.solutions.drawing_utils
 
#To access speaker through the library pycaw 
  devices = AudioUtilities.GetSpeakers()
  interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
  volume = cast(interface, POINTER(IAudioEndpointVolume))
  volbar=400
  volper=0
 
  volMin,volMax = volume.GetVolumeRange()[:2]
 
  while True:
      success,img = cap.read() #If camera works capture an image
      imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #Convert to rgb
    
    #Collection of gesture information
      results = hands.process(imgRGB) #completes the image processing.
 
      lmList = [] #empty list
      if results.multi_hand_landmarks: #list of all hands detected.
        #By accessing the list, we can get the information of each hand's corresponding flag bit
          for handlandmark in results.multi_hand_landmarks:
              for id,lm in enumerate(handlandmark.landmark): #adding counter and returning it
                # Get finger joint points
                  h,w,_ = img.shape
                  cx,cy = int(lm.x*w),int(lm.y*h)
                  lmList.append([id,cx,cy]) #adding to the empty list 'lmList'
              mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)
    
      if lmList != []:
        #getting the value at a point
                        #x      #y
          x1,y1 = lmList[4][1],lmList[4][2]  #thumb
          x2,y2 = lmList[8][1],lmList[8][2]  #index finger
        #creating circle at the tips of thumb and index finger
          cv2.circle(img,(x1,y1),13,(255,0,0),cv2.FILLED) #image #fingers #radius #rgb
          cv2.circle(img,(x2,y2),13,(255,0,0),cv2.FILLED) #image #fingers #radius #rgb
          cv2.line(img,(x1,y1),(x2,y2),(255,0,0),3)  #create a line b/w tips of index finger and thumb
 
          length = hypot(x2-x1,y2-y1) #distance b/w tips using hypotenuse
 # from numpy we find our length,by converting hand range in terms of volume range ie b/w -63.5 to 0
          vol = np.interp(length,[30,350],[volMin,volMax]) 
          volbar=np.interp(length,[30,350],[400,150])
          volper=np.interp(length,[30,350],[0,100])
        
        
          print(vol,int(length))
          volume.SetMasterVolumeLevel(vol, None)
        
        # Hand range 30 - 350
        # Volume range -63.5 - 0.0
        #creating volume bar for volume level 
          cv2.rectangle(img,(50,150),(85,400),(0,0,255),4) # vid ,initial position ,ending position ,rgb ,thickness
          cv2.rectangle(img,(50,int(volbar)),(85,400),(0,0,255),cv2.FILLED)
          cv2.putText(img,f"{int(volper)}%",(10,40),cv2.FONT_ITALIC,1,(0, 255, 98),3)
        #tell the volume percentage ,location,font of text,length,rgb color,thickness
      cv2.imshow('Image',img) #Show the video 
      if cv2.waitKey(1) & 0xff==ord(' '): #By using spacebar delay will stop
          break
        
  cap.release()     #stop cam       
cv2.destroyAllWindows() #close window

 
 
 

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


def voiceChange(v):
    x = int(v)
    assistant.setProperty('voice', voices[x].id)
    speak("Voice is changed sir!")


def shutDown():
    speak("wait a second sir!")
    time.sleep(3)
    pyautogui.click(x=818 , y=1042)
    time.sleep(3)
    pyautogui.click(x=1276, y=975)
    time.sleep(3)
    pyautogui.click(x=1265, y=868)
    time.sleep(3)
    pyautogui.click(x=1265, y=868)
    speak("Done sir!")






speak("hello sir")
speak("i am online")
order = takeCommand()


if "hello" in order:
    speak("Hello sir, tell me what can i do for you?")
    taskExe()
    
