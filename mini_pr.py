
################ This is the code of desktop personal assistant #######################

# psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. It is useful mainly for system monitoring, profiling and limiting process resources and management of running processes.

#@@@@@@@ import modules @@@@@@@#

import pyttsx3                       ## text to speech
import datetime                      ## for data and time
import speech_recognition as sr      ## recogniting the speech from the user
import wikipedia                     ## to access the wekipedia
import smtplib                       ## SMTP handles sending e-mail and routing e-mail between mail servers.
import webbrowser,requests           ## allow displaying web-based documents to users
import os                            ## access the directory
import pyautogui                     ## Used to programmatically control the mouse & keyboard
import psutil                        
import pyjokes                       ## access the jokes and using the functions get_joke &get_jokes.
import cv2,time 
import subprocess
import pywhatkit                     




engine = pyttsx3.init()



#@@@@@@@@@@@@@  Speech function  @@@@@@@@@@@@@#

def speech(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()                 # It make speech audible in the system 



#@@@@@@@@@@@@@  take Instructions  @@@@@@@@@@@@@#

def takeInstructions():
    rec=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        audio = rec.listen(source)
    try:
        print("Recognising...")
        Instruction = rec.recognize_google(audio, language='en-in')
        print(Instruction)
    except Exception as exeptions:
        print(exeptions)
        speech("Say that again please...")
        return "None"
    return Instruction



#@@@@@@@@@@@@@  function for greatings  @@@@@@@@@@@@@#

def greatings():
    speech("Hello")
    speech("I am AURA, your personal desktop companion")


def response():
    speech("I am fine, Thank you")
    speech("How are you, Sir")
 




#@@@@@@@@@@@@@ function for time   @@@@@@@@@@@@@#

def time():
    # strf is used to represent date and time objects into string representation
   
    TimeRightNow=datetime.datetime.now().strftime("%I:%M:%S")  
    hour=0
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        phase="morning"
    elif hour>=12 and hour<18:
        phase="afternoon"
    elif hour>=18 and hour<=24:
        phase="evening"
    else:
        phase="night"
    speech("Its " + TimeRightNow+" of "+phase)



#@@@@@@@@@@@@@ function to inform date  @@@@@@@@@@@@@#

def date():
    YYYY=int(datetime.datetime.now().year)
    MM=int(datetime.datetime.now().month)
    DD=int(datetime.datetime.now().day)
    speech("current date is "+str(DD)+" "+str(MM)+" "+str(YYYY))



#@@@@@@@@@@@@@  function to inform cpu status  @@@@@@@@@@@@@#

def CPUstatus():
    usage=str(psutil.cpu_percent())
    speech('Current CPU usage is at '+usage + "%")
    battery = psutil.sensors_battery()
    speech("Battery remaining is " + str(battery.percent)+"%")
    hdd = psutil.disk_usage('/')
    hddusage=(hdd.used/hdd.total)*100
    hddusage=round(hddusage,2)
    speech("Storage used in C Drive is "+str(hddusage)+"%")
    frequency=psutil.cpu_freq()
    speech("Current frequency of CPU is "+str(frequency.current)+" Megha Hetz")
    RAMused=psutil.virtual_memory().percent
    speech("RAM used is "+str(RAMused)+"%")



#@@@@@@@@@@@@@  function to get jokes  @@@@@@@@@@@@@#

def jokes():
    speech(pyjokes.get_joke())



#@@@@@@@@@@@@@ function to take screenshot  @@@@@@@@@@@@@#

def screenshot():
    img = pyautogui.screenshot()
    speech("By what name should I save it?")
    ans=takeInstructions()
    #Replace FolderPath with the path of folder where you want to save your screenshots in your computer 
    ans="FolderPath"+ans+".png"
    img.save(ans)
    speech("Screenshot taken")


#@@@@@@@@@@@@@  function to take picture  @@@@@@@@@@@@@#

def camera():
    speech("Press space to take image and escape to stop Camera")
    Camera = cv2.VideoCapture(0)
    cv2.namedWindow("Camera")
    img_counter = 0
    while True:
        ret, frame = Camera.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("Camera", frame)
        k = cv2.waitKey(1)
        if k%256 == 27:
            speech("closing camera")
            break
        elif k%256 == 32:
            img_name = "camera{}.png".format(img_counter)
            #Replace CameraPath with the path of the folder where you want to save your photos taken by camera
            path="CameraPath"
            cv2.imwrite(os.path.join(path , img_name), frame)
            cv2.imwrite(img_name, frame)
            speech("{} image taken".format(img_name))
            img_counter += 1
    Camera.release()
    cv2.destroyAllWindows() 


#@@@@@@@@@@@@@@@@@     Function to access wikipedia     @@@@@@@@@@@@@@@#


def Wikipedia(query):
    speech("Searching...")
    query=query.replace("wikipedia","")
    result = wikipedia.summary(query,sentences=2)
    speech(result)

#@@@@@@@@@@@@@@@@@     Function to access websites     @@@@@@@@@@@@@@@#

def OpenWebsite():
    speech("Which website should i open?")
    # Replace ChromePath with  path of chrome.exe in your computer in the line below where it is written  
    path='ChromePath  %s' 
    website=takeInstructions().lower()
    webbrowser.get(path).open_new_tab(website+'.com')


#@@@@@@@@@@@@@@@@@     Function to access Google      @@@@@@@@@@@@@@@#


def GoogleSearch():
    speech("What should I search?")
    SearchData=takeInstructions()
    webbrowser.open(SearchData)
    speech("Here is the search result")  


#@@@@@@@@@@@@@@@@@     Function to access Song Directory     @@@@@@@@@@@@@@@#


def Songs():
    #Replace MusicPath with the path of the folder where you want to save the music that you want it to play
    songs_dir='C:\\Users\\hp\\Music\\new songs'
    playsongs=os.listdir(songs_dir)
    os.startfile(os.path.join(songs_dir,playsongs[0]))


#@@@@@@@@@@@@@@@@@     Function to Rememeber the Data      @@@@@@@@@@@@@@@#


def Remember():
    speech("What should I remember?")
    Information=takeInstructions()
    speech('you said me to remember that '+Information)
    rem = open('data.txt','w') 
    rem.write(Information) 
    rem.close()  




#@@@@@@@@@@@@@@@@@     Function to give output of rememebered Data     @@@@@@@@@@@@@@@#


def Knowing():
    remember=open('data.txt','r')
    speech("you said me to remember that"+remember.read())




#@@@@@@@@@@@@@@@@@     Function to access Weather Report     @@@@@@@@@@@@@@@#

def Weather():
    speech("Which city's weather you want to know?")
    city=takeInstructions().lower()
    # Replace YourAPIkey by your API key in line below which you get after signing in in https://openweathermap.org/
    url="://api.openweathermap.org/data/2.5/weahttpther?q={}&appid=YourAPIkey".format(city)
    res=requests.get(url)
    data=res.json()
    climate=data["weather"][0]["description"]
    speech("Todays climate is "+climate)
    temp=data['main']['temp']
    temp=round(temp-273.15,2)
    speech("Average Temperature is "+str(temp)+" Degree Celcius")
    maxtemp=data['main']['temp_max']
    maxtemp=round(maxtemp-273.15,2)
    speech("Maximum temperature is "+ str(maxtemp)+" Degree Celcius")
    mintemp=data['main']['temp_min']
    mintemp=round(mintemp-273.15,2)
    speech("Minimum temperature is "+ str(mintemp)+ " Degree Celcius")
    wind=data["wind"]["speed"]
    speech("WindSpeed is "+str(wind)+" meters per second")
    humidity=data["main"]["humidity"]
    speech("Humidity is "+str(humidity)+"%")
    visibile=data["visibility"]
    speech("Visibitity is "+str(visibile)+" meters")
    cloud=data["clouds"]["all"]
    speech("Its "+str(cloud)+" percent cloudy")
    pressure=data['main']["pressure"]
    speech("Air pressure is at "+ str(pressure)+"hpa")




def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()



def send_whatsapp_message():
    speech("tell me the mobile number where you want to send message")
    phone_number = takeInstructions().lower()
    speech("tell me the message that you want to send")
    message=takeInstructions().lower()
    speech("tell me the hour")
    hour=takeInstructions().lower()
    speech("tell me seconds")
    second=takeInstructions().lower()
    pywhatkit.sendwhatmsg(phone_number,message,hour,second)



def opencmd():
    os.system('start cmd')


def openCalculator():
    calculator = "C:\\Windows\\System32\\calc.exe"
    subprocess.Popen('calculator')


def play_on_youtube():
    webbrowser.open_new_tab("https://www.youtube.com")
    # speech("youtube is open now")
    # time.sleep(0)

def location():
    listening = True
    query = query.split(" ")
    location_url = "https://www.google.com/maps/place/" + str(query[2])
    response("Hold on Dante, I will show you where " + query[2] + " is.")
    maps_arg = '/usr/bin/open -a "/Applications/Google Chrome.app" ' + location_url
    os.system(maps_arg)









#@@@@@@@@@@@@@@@@@     Function provided for User's help     @@@@@@@@@@@@@@@#

def help():
    speech("Here are the keywords that should be in your command for following work to be done")
    speech("MY INTRODUCTION to repeat my introduction")
    speech("TIME to get time")
    speech("DATE to get date")
    speech("CPU STATUS to get information about present condition of CPU")
    speech("JOKE to listen a joke")
    speech("SCREENSHOT to get screenshot")
    speech("CAMERA to click photos of you in webcam")
    speech("WIKIPEDIA to get do wikipedia search")
    speech("OPEN WEBSITE to open website")
    speech("SEARCH to do google search")
    speech("SONG to start a song")
    speech("REMEMBER if you want me to remember something")
    speech("KNOW if you want me to tell you what you have asked me to remember earlier")
    #speech("WEATHER to know a weather forcast")
    speech(" and speak HELP to repeat these thing again")



#      ************************************      Main Function      *****************************************

if __name__ == '__main__':
    greatings()
    speech("I am ready to take command")  
    speech("Say help to know all my features else continue to give command ")
    while True:
        query = takeInstructions().lower()
        if 'my introduction' in query:
            greatings()
        elif 'how are you' in query:
            response()
        elif 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'cpu status' in query:
            CPUstatus()
        elif 'joke' in query:
            jokes()
        elif 'screenshot' in query:
            screenshot()
        elif 'camera' in query:
            camera()
        elif 'wikipedia' in query:
            Wikipedia(query)
        elif 'open website' in query:
            OpenWebsite()
        elif 'search' in query:
            GoogleSearch()
        elif 'song' in query:
            Songs()
        elif 'where is' in query:
            location()
        elif 'remember' in query:
            Remember()
        elif 'know' in query:
            Knowing()
        elif 'weather' in query:
            Weather()
        elif 'help' in query:
            help()

        elif 'offline' or 'quit' or 'bye bye' or 'good night' in query:
            break
    speech("Shutting Down. Have a nice day!")