import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import time
import wikipedia
import pyjokes
import requests
import cv2
import webbrowser
import os
from dotenv import load_dotenv
# Load the .env file
load_dotenv()


# Ensure pysong is correctly imported
try:
    import pysong
except ImportError:
    pysong = None
    print("pysong module not found. Please install it.")

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'priya' in command:
                command = command.replace('priya', '')
                print(command)
    except sr.UnknownValueError:
        talk("Sorry, I did not catch that. Could you repeat?")
    except sr.RequestError:
        talk("Sorry, there was an issue with the speech recognition service.")
    return command

def send_whatsapp_message(contact, message):
    try:
        # Ensure the contact is in the correct format (e.g., "+1234567890" for international numbers)
        pywhatkit.sendwhatmsg_instantly(contact, message)
        talk(f'Sending WhatsApp message to {contact}.')
    except Exception as e:
        talk(f"An error occurred while sending the message: {e}")

def open_camera():
    cap = cv2.VideoCapture(0)  # 0 is the default camera
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break
    cap.release()
    cv2.destroyAllWindows()

def open_youtube():
    webbrowser.open("https://www.youtube.com/")

def open_google():
    webbrowser.open("https://www.google.com")

def personalized_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        talk("Good morning! dear How can I assist you today?")
    elif 12 <= hour < 18:
        talk("Good afternoon!dear How can I assist you today?")
    else:
        talk("Good evening! dear How can I assist you today?")
    
def set_reminder(reminder, remind_time):
    current_time = datetime.datetime.now().strftime('%H:%M')
    while current_time != remind_time:
        current_time = datetime.datetime.now().strftime('%H:%M')
        time.sleep(30)  # Check every 30 seconds
    talk(f"Reminder: {reminder}")

def validate_time_format(time_str):
    try:
        datetime.datetime.strptime(time_str, '%H:%M')
        return True
    except ValueError:
        return False

import requests

def get_weather(city):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Construct the full URL with city and API key
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if response.status_code == 200:
        # If the response is successful, try to access the weather data
        try:
            main = data["main"]
            temperature = main["temp"]
            weather_description = data["weather"][0]["description"]
            talk(f"The temperature in {city} is {temperature} degrees Celsius with {weather_description}.")
        except KeyError:
            talk("Unexpected data format from the weather service. Please try again.")
    else:
        # If the API returns an error (e.g., city not found), handle it here
        talk("City not found or there was an issue with the weather service. Please try again.")
def ask_gemini(query):
    # Replace with your actual Gemini API endpoint and key
    api_key = os.getenv('GEMINI_API_KEY')
    endpoint = os.getenv('GEMINI_API_ENDPOINT')    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        'query': query
    }
    
    try:
        response = requests.post(endpoint, headers=headers, json=payload)
        response.raise_for_status()
        return response.json().get('answer', 'Sorry, I could not find an answer.')
    except requests.exceptions.RequestException as e:
        return f"Error connecting to Gemini API: {e}"

def run_priya():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + current_time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        try:
            info = wikipedia.summary(person, sentences=1) 
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError:
            talk("There are multiple results for that query. Please be more specific.")
        except wikipedia.exceptions.PageError:
            talk("I couldn't find any information on that topic.")
    elif 'date me' in command:
        talk('Sorry, I have a headache.')
    elif 'remind me to' in command:
        # Get reminder message from the user via input field
        reminder = input("What should I remind you to do? ").strip()
        
        # Loop until a valid time format is entered
        while True:
            remind_time = input("At what time? Please specify in HH:MM format: ").strip()
            if validate_time_format(remind_time):
                break
            else:
                talk("The time format is invalid. Please enter the time in HH:MM format.")

        # Confirmation message
        talk(f"Setting a reminder for {reminder} at {remind_time}.")

        # Set the reminder
        set_reminder(reminder, remind_time)
    elif 'are you single' in command:
        talk('I am single. Did you love me?')
    elif 'hey priya' in command:
        talk('Hi dear, how can I help you?')
    elif 'good morning' in command:
        talk('Good morning! How are you today?')
    elif 'good afternoon' in command:
        talk('Good afternoon! How are you today? Did you have lunch?')
    elif 'i love you' in command:
        talk('I love you too!')
    elif 'how was the day' in command:
        talk('Today is a good day. How about you?')
    elif 'have you had lunch' in command:
        talk('Yes, today I had a nice lunch with rice and fish curry.')
    elif 'open camera' in command:
        talk('Opening camera.')
        open_camera()
    elif 'hello' in command or 'hi' in command:
        personalized_greeting()
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'weather in' in command:
        city = command.replace('weather in', '').strip()
        talk(f"Checking weather for {city}")
        get_weather(city)
    elif 'song' in command:
        if pysong:
            try:
                song_info = pysong.get_song()
                talk(song_info)
            except AttributeError:
                talk("The function get_song() does not exist in the pysong module.")
            except Exception as e:
                talk(f"An error occurred: {e}")
        else:
            talk("The pysong module is not available.")
    elif 'send' in command and 'message' in command:
        contact = input('Please type the contact name or number (with country code): ')
        talk(f'What is the message for {contact}?')
        message = take_command()
        send_whatsapp_message(contact, message)
    elif 'ask' in command:
        query = command.replace('ask', '').strip()
        talk('Let me find the answer for you.')
        answer = ask_gemini(query)
        talk(answer)
    elif 'will you marry me' in command:
        talk('Did you promise me you will not cheat?')
    elif 'open youtube' in command or 'open YouTube' in command:
        talk('Opening YouTube.')
        open_youtube()
    elif 'open google' in command or 'open Google' in command:
        talk('Opening Google.')
        open_google()
    elif 'gemini' in command:
        query = command.replace('gemini', '')
        answer = ask_gemini(query.strip())
        talk(answer)
    elif 'open notepad' in command:
        talk('Opening Notepad.')
        os.system('notepad')
    elif 'open ads' in command or 'open microsoft edge' in command:
        talk('Opening Microsoft Edge.')
        try:
            result = os.system('start msedge')  # Windows command
            if result != 0:
                talk('Failed to open Microsoft Edge.')
            else:
                talk('Microsoft Edge should now be open.')
        except Exception as e:
            talk(f'An error occurred: {e}')
    elif 'open word' in command:
        talk('Opening Microsoft Word.')
        try:
            # Use the appropriate command for your OS
            result = os.system('start winword')  # Windows command; replace for other OS
            if result != 0:
                talk('Failed to open Microsoft Word.')
            else:
                talk('Microsoft Word should now be open.')
        except Exception as e:
            talk(f'An error occurred: {e}')
    elif 'open whatsapp' in command:
        talk('Opening WhatsApp.')
        try:
            result = os.system('start whatsapp')  # Windows command; replace for other OS
            if result != 0:
                talk('Failed to open WhatsApp.')
            else:
                talk('WhatsApp should now be open.')
        except Exception as e:
            talk(f'An error occurred: {e}')

    elif 'open vs code' in command:
        talk('Opening Visual Studio Code.')
        os.system('code')
    elif 'open excel' in command:
        talk('Opening Microsoft Excel.')
        try:
            # Use the appropriate command for your OS
            result = os.system('start excel')  # Windows command; replace for other OS
            if result != 0:
                talk('Failed to open Microsoft Excel.')
            else:
                talk('Microsoft Excel should now be open.')
        except Exception as e:
            talk(f'An error occurred: {e}')
    elif 'open powerpoint' in command:
        talk('Opening Microsoft PowerPoint.')
        try:
            # Use the appropriate command for your OS
            result = os.system('start powerpnt')  # Windows command; replace for other OS
            if result != 0:
                talk('Failed to open Microsoft PowerPoint.')
            else:
                talk('Microsoft PowerPoint should now be open.')
        except Exception as e:
            talk(f'An error occurred: {e}')
    elif 'shutdown system' in command:
        talk('Shutting down the system.')
        os.system('shutdown /s /t 1')  # Sh
    else:
        talk('Please say the command again.')

while True:
    run_priya()
