import speech_recognition as sr
import datetime
import pyttsx3
import subprocess
import pywhatkit 
 

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)
engine.say("Hey,I am your alexa")
print("Hey,I am your alexa")
engine.say("how may i help you.....")
print("how may i help you.....")
engine.runAndWait()

engine.setProperty('voice', voices[1].id) 
recognizer = sr.Recognizer()


def take_command():
    """Captures voice input and performs speech recognition."""
    print("Clearing background noise...")
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        recorded_audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(recorded_audio, language="en-US")
        print("You said:", command)
        return command.lower()  
    except Exception as ex:
        print(ex)
        print("Could not understand your voice. Please try again.")
        return None


def run_alexa():
    """Executes tasks based on voice commands."""
    while True:
        command = take_command()
        if not command:
            continue

        if " open the chrome" in command:
            chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe" 
            subprocess.Popen([chrome_path])
            engine.say("Opening Chrome...")
            engine.runAndWait()

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print(current_time)
            engine.say(current_time)
            engine.runAndWait()
           
        
        elif "play" in command:
            video_title = command.split("play ")[1]  
            engine.say("Opening YouTube and playing " + video_title)
            engine.runAndWait()
            try:
                pywhatkit.playonyt(video_title)  
            except Exception as ex:  
                print(f"Error playing video: {ex}")
                print("Opening YouTube for manual search...")
                subprocess.Popen(["https://www.youtube.com/"])  # Open YouTube in browser

        elif "exit" in command:
            print("Exiting...")
            engine.say("Goodbye and see you again")
            print("Goodbye and see you again")
            engine.runAndWait()
            break


if __name__ == "__main__":
    run_alexa()
