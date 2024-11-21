import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests  # For connecting to APIs

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

def search_wikipedia(query):
    try:
        info = wikipedia.summary(query, sentences=1)
        return info
    except wikipedia.exceptions.DisambiguationError:
        return "There are multiple results for that query. Please be more specific."
    except wikipedia.exceptions.PageError:
        return "I couldn't find any information on that topic."

def ask_gemini(query):
    # Replace 'your_api_key' and 'your_endpoint' with your actual API details
    api_key = 'AIzaSyBdtBkXs14EfmtuetApc4lQq1aZs7ZpEik'
    endpoint = 'https://api.yourservice.com/query'
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        'query': query
    }
    
    response = requests.post(endpoint, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json().get('answer', 'Sorry, I could not find an answer.')
    else:
        return "There was an error connecting to the API."

def run_priya():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = search_wikipedia(person)
        print(info)
        talk(info)
    elif 'ivf' in command:
        question = command.replace('ivf', '')
        talk('Searching for an answer to your question.')
        answer = ask_gemini(question)  # or use search_wikipedia(question)
        print(answer)
        talk(answer)
    elif 'date me' in command:
        talk('Sorry, I have a headache.')
    elif 'heloo' in command:
        talk('Hi Priyan!')
    elif 'are you single' in command:
        talk('I am single. Did you love me?')
    elif 'i love you' in command:
        talk('I love you too!')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'will you marry me' in command:
        talk('Did you promise me you will not cheat?')
    else:
        talk('Please say the command again.')

while True:
    run_priya()
