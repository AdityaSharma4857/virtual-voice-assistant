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
import pywhatkit
import pyjokes
from tkinter import *
import keyboard
from playsound import playsound
from PIL import ImageTk, Image

name_file = open("Assistant_name", "r")
name_assistant = name_file.read()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(text):
    engine.say(text)
    print(name_assistant + " : " + text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello, Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")

def askname():
    speak("What is your name dear?")
    name = takeCommand()
    speak("Welcome " + name)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source, timeout=30, phrase_time_limit=5)

        try:
            print("Recognizing...")
            statement=r.recognize_google(audio,language='en-in')
            print(f"User said:{statement}\n")

        except Exception as e:
            print('Unable to Recognize your voice.')
            speak("Unable to Recognize your voice.")
            return "None"
        return statement


def Process_audio():
    run = 1
    while run == 1:
        speak("Hi, I'm your personal assistant - " + name_assistant)
        wishMe()
        askname()
        speak("How can I help you?")
        run +=1

    if __name__=='__main__':

        while True:
            
            statement = takeCommand().lower()

            if "goodbye" in statement or "bye" in statement or "stop" in statement or 'exit' in statement:
                speak('Your personal assistant ' + name_assistant + ' is shutting down, Good bye')
                screen.destroy()
                break

            elif 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(10)

            elif 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google chrome is open now")
                time.sleep(10)

            elif 'open gmail' in statement:
                webbrowser.open_new_tab("https://www.gmail.com")
                speak("Google Mail open now")
                time.sleep(10)

            elif "open notepad" in statement:
                speak("Opening notepad")
                path= "c:\\windows\\system32\\notepad.exe"
                os.startfile(path)
                time.sleep(10)

            elif "close notepad" in statement:
                speak("Closing notepad")
                os.system("TASKKILL /F /IM notepad.exe") 

            elif "open calculator" in statement:  # -----------> Working fine but once opened it not gets closed by voice command
                speak("Opening calculator")
                path= "c:\\windows\\system32\\calc.exe"
                os.startfile(path)
                time.sleep(5)

            elif "open chrome" in statement:
                speak("Opening chrome")
                path= "C:\Program Files\Google\Chrome\Application\chrome.exe"
                os.startfile(path)
                time.sleep(10)

            elif "close chrome" in statement:
                speak("Closing chrome")
                os.system("TASKKILL /F /IM chrome.exe")

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
                    speak(" Temperature in kelvin unit = " +
                        str(current_temperature) +
                        "\n humidity (in percentage) = " +
                        str(current_humidiy) +
                        "\n description = " +
                        str(weather_description))

                else:
                    speak(" City Not Found ")
            
            elif 'play' in statement:
                song = statement.replace('play', '')
                speak('playing' + song)
                pywhatkit.playonyt(song)
                time.sleep(10)

            elif "song" in statement:
                speak("Which song will you like to hear")

            elif 'how are you' in statement:
                speak("I am fine, Thank you")
                speak("How are you")
    
            elif 'fine' in statement or "good" in statement:
                speak("It's good to know that your fine")

            elif 'good morning' in statement:
                speak("A very good morning dear")

            elif 'good afternoon' in statement:
                speak("Good afternoon dear")

            elif 'good night' in statement:
                speak("A very good night dear, sweet dreams")

            elif 'robot' in statement:
                speak("I don't have any robotic parts - I'm software that runs on your phone and desktops")

            elif "where is" in statement:
                statement = statement.replace("where is", "")
                location = statement
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.com/maps/place/" + location + "")

            elif 'time' in statement:
                strTime=datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The time is {strTime}")

            elif 'who are you' in statement or 'what can you do' in statement:
                speak('I am ' + name_assistant + 'version 1 point O your personal assistant. I am programmed to minor tasks like'
                    'opening youtube, google chrome, gmail and stackoverflow, predict time, take a photo, search wikipedia, predict weather' 
                    'in different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')


            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                speak("I was built by Aditya, Vishnu And Prachiti")

            elif 'for date' in statement:   
                speak('Sorry, I have a headache. Ask to Siri, she might come with you')
        
            elif 'are you single' in statement:
                speak("yes baby, just like you")

            elif 'i love you' in statement:
                speak("Sorry, I'm in relationship with Siri")

            elif "open stackoverflow" in statement:
                webbrowser.open_new_tab("https://stackoverflow.com/login")
                speak("Here is stackoverflow")
                time.sleep(10)

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

            elif 'joke' in statement or 'entertain' in statement:
                print("Here is a joke for you :")
                joke = pyjokes.get_joke()
                speak(joke)
                time.sleep(5)

            elif 'ask' in statement:
                speak('Yes, I can answer to computational and geographical questions and what question do you want to ask now')
                question = takeCommand()
                app_id = "R2K75H-7ELALHR35X"
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)

            elif 'wikipedia' in statement or 'who is' in statement or "what is" in statement:
                speak('Searching Wikipedia...')
                statement =statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                speak(results)

            elif "log off" in statement or "sign out" in statement:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

            elif 'shutdown' in statement:
                speak("Hold on a sec! Your system is on its way to shutdown")
                subprocess.call(["shutdown", "/s"])

            elif 'restart' in statement:
                speak("Your system will restart now")
                subprocess.call(["shutdown", "/r"])

            elif "bored" in statement:
                speak("I'm here to do cool tasks for you")
                speak("What should I do")
                speak("Should I play a song or tell you a joke")

            elif 'what are you doing' in statement:
                speak("Nothing dear, I'm here to help you.")
                speak("Tell me what should I do for you")

            elif 'hello' in statement:
                speak("Hello dear, have a good day")

            elif 'thank you' in statement:
                speak("I'm honoured to serve")

            elif 'what is your name' in statement:
                speak('Well, my name is ' + name_assistant + ', I wish everyone have a good name as mine')

            else:
                speak("Please say it again")


def change_name():

  name_info = name.get()

  file=open("Assistant_name", "w")

  file.write(name_info)

  file.close()

  settings_screen.destroy()

  screen.destroy()

def change_name_window():
    
    global settings_screen
    global name


    settings_screen = Toplevel(screen)
    settings_screen.title("Settings")
    settings_screen.geometry("500x500")
    settings_screen.iconbitmap('app_icon.ico')

      
    name = StringVar()

    current_label = Label(settings_screen, text = "Current name: " + name_assistant)
    current_label.pack()

    enter_label = Label(settings_screen, text = "Please enter your Virtual Assistant's name below")
    enter_label.pack(pady=10)
      

    Name_label = Label(settings_screen, text = "Name")
    Name_label.pack(pady=10)
     
    name_entry = Entry(settings_screen, textvariable = name)
    name_entry.pack()


    change_name_button = Button(settings_screen, text = "Ok", width = 10, height = 1, command = change_name)
    change_name_button.pack(pady=10)

def info():

    info_screen = Toplevel(screen)
    info_screen.title("Info")
    info_screen.iconbitmap('app_icon.ico')
    info_screen.geometry("300x100+800+350")

    creator_label = Label(info_screen,text = "Created by Aditya Sharma")
    creator_label.pack(pady=10)

    for_label = Label(info_screen, text = "For Python mini project")
    for_label.pack()

    keyboard.add_hotkey("F4", Process_audio)

def wikipedia_screen(text):


    wikipedia_screen = Toplevel(screen)
    wikipedia_screen.title(text)
    wikipedia_screen.iconbitmap('app_icon.ico')

    message = Message(wikipedia_screen, text = text)
    message.pack()


def main_screen():

    global screen
    screen = Tk()
    screen.title("Virtual Voice Assistant - " + name_assistant)
    screen.geometry("1100x750+400+100")
    screen.iconbitmap('app_icon.ico')

    frame = Frame(screen, width=50, height=25)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    img = ImageTk.PhotoImage(Image.open("assistant.jpg"))
    label = Label(frame, image = img)
    label.pack()

    name_label = Label(text = name_assistant, font = ("Calibri", 30))
    name_label.place(x=500, y=530)

    microphone_photo = PhotoImage(file = "microphone.png")
    microphone_button = Button(image=microphone_photo, command = Process_audio)
    microphone_button.place(x=525, y=665)

    settings_photo = PhotoImage(file = "settings.png")
    settings_button = Button(image=settings_photo, command = change_name_window)
    settings_button.place(x=425, y=665)
        
    info_photo = PhotoImage(file = "info.png")
    info_button = Button(image =info_photo, command = info, font = ("Calibri", 15))
    info_button.place(x=625, y=665)

    screen.mainloop()


main_screen()

