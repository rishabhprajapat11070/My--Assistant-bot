import speech_recognition as sr 
import pyaudio
import pyttsx3 
import os
import webbrowser
import google.generativeai as genai

genai.configure(api_key="AIzaSyC8XODS3NjzcLZDYJuipcHHdRpiZcVwZqw")
model = genai.GenerativeModel("gemini-1.5-flash")

def talk2(text):
    say=gTTS(text=text,lang="hi")
    say.save("say.mp3")
    os.system("say.mp3")

def talk(text):
    engin = pyttsx3.init()
    engin.say(text)
    engin.runAndWait()
    
def prosseing_data(c):
    
    if(c == "open google"):
        talk("opening google")
        webbrowser.open("https://google.com")
    elif(c == "open youtube"):
        talk("opening youtube")
        webbrowser.open("https://youtube.com")

    elif(c == "open chat gpt"):
        talk("opening chatgpt")
        webbrowser.open("https://chatgpt.com")
        
    elif(c == "open google"):
        talk("opening google")
        webbrowser.open("https://google.com")
        
    elif(c):
        response = model.generate_content(c)
        talk(response.text)
        print(response.text)
          
    else:
        talk("notfound")
    
    
reco = sr.Recognizer()
talk("init Rico")
while True:
    try:
        with sr.Microphone() as mic:
            print("speak...")
            reco.adjust_for_ambient_noise(mic) 
            audio= reco.listen(mic)  
            text=reco.recognize_google(audio,language="en")
            print(text)
            
            if(text=="Rico"):
                talk("yaa")
                print("mega active..")
                with sr.Microphone() as mic :
                    reco.adjust_for_ambient_noise(mic)
                    here=reco.listen(mic)
                    command = reco.recognize_google(here)
                    print(command.lower())
                    prosseing_data(command.lower())
                       
    except sr.UnknownValueError:
        print("not here...")
    except :
        print("networks error.......")
        
    
    
        
        

       
     
    
        

   
    
    



