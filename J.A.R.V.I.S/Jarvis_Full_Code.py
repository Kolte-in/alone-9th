import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import pyautogui
import requests
from pywikihow import search_wikihow
import datetime
import random
from bs4 import BeautifulSoup
import psutil
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import nltk
from keyboard import write
from pyautogui import click
from keyboard import press_and_release
from os import startfile

from googletrans import Translator
from gtts import gTTS
import speedtest
from transformers import pipeline


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Define Google API key and search engine ID
API_KEY = open("API_KEY").read()
SEARCH_ENGINE = open("X").read()

# Define news API key
NEWS_API_KEY = open("NEWS_API").read()

# Define weather API key
WEATHER_API_KEY = open("WEATHER-API").read()






def speak(audio):
    """Function to speak the given audio"""
    print("     ")
    engine.say(audio)
    engine.runAndWait()
    print(f"Jarvis : {audio}")
    print("     ")
def wish_me():
    """Function to greet the user"""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        greeting = "Good Morning Sir"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon Sir"
    else:
        greeting = "Good Evening Sir"
    speak(greeting + ", " + random_greeting())
def random_greeting():
    """Function to generate a random greeting"""
    greetings = [
        "Jarvis here, at your service.",
        "Greetings, I'm Jarvis. What task can I tackle for you?",
        # Add more greetings here...
    ]
    return random.choice(greetings)
def take_Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()  # Return the recognized query
    except Exception as e:
        print("Say that again please...")
        # Return an empty string if no speech is detected
def search_and_speak(query):
    """Function to search Google, open the first link, and speak the main content"""
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'q': query,
        'key': API_KEY,
        'cx': SEARCH_ENGINE
    }
    response = requests.get(url, params=params)
    results = response.json()
    if 'items' in results:
        first_link = results['items'][0]['link']
        print("First link:", first_link)
        # Fetching content from the webpage
        page = requests.get(first_link)
        soup = BeautifulSoup(page.content, 'html.parser')
        # Extracting and cleaning the main content
        main_content = soup.get_text(separator='\n')
        # Limiting the content to the first 200 words
        words = main_content.split()[:200]
        limited_content = ' '.join(words)
        # Speaking the content
        engine = pyttsx3.init()
        engine.say(limited_content)
        engine.runAndWait()
        # Ask if the user wants to continue reading
        speak("Do you want to continue reading? ")
def open_youtube_video(video_query):
    """Function to open a video on YouTube"""
    pywhatkit.playonyt(video_query)
def open_gmail():
    """Function to open Gmail in the web browser"""
    webbrowser.open('https://mail.google.com')
def open_microsoft():
    """Function to open Gmail in the web browser"""
    webbrowser.open('https://microsoft.com')
def open_chatgpt():
    """Function to open ChatGPT documentation"""
    webbrowser.open("https://chatgpt.com")
def get_news(api_key, source):
    url = f"https://newsapi.org/v2/top-headlines?sources={source}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "ok":
        articles = data["articles"]
        return articles
    else:
        speak("sorry sir, i didnt catch that")
def read_news():
    news_phrases = [
        "Retrieving the latest news articles... Please wait!",
        "Gathering the most recent news articles... Please wait!",
        "Obtaining the freshest news articles... Please wait!",
        "Acquiring the newest news articles... Please wait!",
        "Collecting the latest news updates... Please wait!",
        "Scanning for the most recent news articles... Please wait!",
        "Searching for the freshest news updates... Please wait!",
        "Seeking out the newest news articles... Please wait!",
        "Finding the latest news stories... Please wait!",
        "Locating the most recent news updates... Please wait!",
        "Hunting down the freshest news articles... Please wait!",
        "Sourcing the newest news stories... Please wait!",
        "Discovering the latest news reports... Please wait!",
        "Uncovering the most recent news updates... Please wait!",
        "Digging up the freshest news articles... Please wait!",
        "Exploring the latest news releases... Please wait!",
        "Examining the most recent news stories... Please wait!",
        "Investigating the freshest news updates... Please wait!",
        "Reviewing the latest news headlines... Please wait!",
        "Analyzing the most recent news articles... Please wait!",
        "Inspecting the freshest news updates... Please wait!",
        "Checking out the latest news stories... Please wait!",
        "Monitoring the most recent news updates... Please wait!",
        "Observing the freshest news articles... Please wait!",
        "Reviewing the latest news reports... Please wait!",
        "Scrutinizing the most recent news updates... Please wait!",
        "Surveying the freshest news articles... Please wait!",
        "Watching the latest news stories... Please wait!",
        "Monitoring the most recent news releases... Please wait!",
        "Observing the freshest news updates... Please wait!"
    ]
    speak(random.choice(news_phrases))
    api_key = open('NEWS_API').read()  # Replace with your NewsAPI API key
    speak("From which source would you like to hear the news? BBC or Times of India? Or something else i have provided a list you can check from that.")

    source_choice = take_Command().lower()
    if "bbc" in source_choice:
        source = "bbc-news"
    elif "times of india" in source_choice:
        source = "the-times-of-india"
    elif "associated press" in source_choice:
        source = "associated-press"
    elif "reuters" in source_choice:
        source = "reuters"
    elif "cnn" in source_choice:
        source = "cnn"
    elif "the new york times" in source_choice:
        source = "the-new-york-times"
    elif "the guardian" in source_choice:
        source = "the-guardian"
    elif "al jazeera" in source_choice:
        source = "al-jazeera-english"
    elif "nbc news" in source_choice:
        source = "nbc-news"
    elif "abc news" in source_choice:
        source = "abc-news"
    elif "usa today" in source_choice:
        source = "usa-today"
    elif "the washington post" in source_choice:
        source = "the-washington-post"
    elif "bloomberg" in source_choice:
        source = "bloomberg"
    elif "business insider" in source_choice:
        source = "business-insider"
    elif "the wall street journal" in source_choice:
        source = "the-wall-street-journal"
    elif "national geographic" in source_choice:
        source = "national-geographic"
    elif "the economist" in source_choice:
        source = "the-economist"
    elif "time" in source_choice:
        source = "time"
    elif "buzzfeed" in source_choice:
        source = "buzzfeed"
    elif "the hindu" in source_choice:
        source = "the-hindu"
    elif "ndtv" in source_choice:
        source = "ndtv"
    elif "indian express" in source_choice:
        source = "the-indian-express"
    elif "hindustan times" in source_choice:
        source = "hindustan-times"
    elif "zee news" in source_choice:
        source = "zee-news"
    elif "times now" in source_choice:
        source = "times-now"
    elif "abp news" in source_choice:
        source = "abp-news"
    elif "the telegraph india" in source_choice:
        source = "the-telegraph-india"
    elif "deccan chronicle" in source_choice:
        source = "deccan-chronicle"
    elif "moneycontrol" in source_choice:
        source = "moneycontrol"
    else:
        speak("I'm sorry, I couldn't recognize that news source. Please try again with a different source.")
        return
    articles = get_news(api_key, source)
    if articles:
        for article in articles:
            if 'title' in article and 'description' in article and 'content' in article:
                title = article['title']
                print(title)
                description = article['description']
                print(description)
                content = article['content']
                print(content)
                # Speak the title and description
                speak(f"Title: {title}")
                speak(f"Description: {description}")

                # Ask if the user wants to read the entire article
                speak("Do you want me to read the entire article?")
                response = take_Command()
                if 'read' in response or 'yes' in response or 'read the article' in response:
                    # Speak the entire content
                    speak(content)
                    continue
                elif 'no' in response or "don't" in response:
                    speak("Alright.")
                    return
                else:
                    speak("Sorry, I didn't catch that.")
                    speak("Would you like to hear the next headline or do something else?")
                    next_command = take_Command()
                    if 'something else' in next_command:
                        sentences = [
                            "Sure, what else can I assist you with?",
                            "Of course, what more can I help you with?",
                            "Certainly, what else may I do for you?",
                            "Absolutely, what else do you need assistance with?",
                            "Sure thing, what else can I do to assist you?",
                            "Certainly, how else may I be of service?",
                            "Of course, what additional assistance do you require?",
                            "Absolutely, what more can I assist you with?",
                            "Sure, what else would you like me to do?",
                            "Of course, what further help can I provide?",
                            "Certainly, what else do you need help with?",
                            "Absolutely, what more can I do for you?",
                            "Sure thing, what else may I assist you with?",
                            "Of course, what else can I do to help?",
                            "Certainly, what else can I assist you with?",
                            "Absolutely, what further assistance do you require?",
                            "Sure, what else would you like me to help with?",
                            "Of course, how else can I assist you?",
                            "Certainly, what more may I do for you?",
                            "Absolutely, what else do you need support with?",
                            "Sure thing, what else can I do for you?",
                            "Of course, what else can I help with?",
                            "Certainly, what else do you need assistance with?",
                            "Absolutely, what further assistance can I provide?",
                            "Sure, what else would you like me to do?",
                            "Of course, what more can I assist with?",
                            "Certainly, what else do you need help with?",
                            "Absolutely, what more can I do for you?",
                            "Sure thing, what else may I assist with?"
                        ]

                        # Randomly choose a sentence
                        random_sentence = random.choice(sentences)

                        # Output the randomly chosen sentence
                        speak(random_sentence)
                        # Perform other actions here based on user's command
                        return
                    else:
                        phrases = [
                            "Transitioning to the subsequent headline.",
                            "Proceeding to the next headline.",
                            "Advancing to the following headline.",
                            "Shifting focus to the next headline.",
                            "Moving forward to the next headline.",
                            "Progressing to the next headline.",
                            "Transitioning to the next headline.",
                            "Continuing to the next headline.",
                            "Proceeding to the subsequent headline.",
                            "Moving on to the subsequent headline.",
                            "Transitioning to the subsequent headline.",
                            "Advancing to the next headline.",
                            "Shifting focus to the subsequent headline.",
                            "Moving forward to the subsequent headline.",
                            "Progressing to the subsequent headline.",
                            "Transitioning to the subsequent headline.",
                            "Continuing to the subsequent headline.",
                            "Proceeding to the next headline.",
                            "Advancing to the subsequent headline.",
                            "Shifting focus to the next headline.",
                            "Moving forward to the subsequent headline.",
                            "Progressing to the next headline.",
                            "Transitioning to the next headline.",
                            "Continuing to the subsequent headline.",
                            "Proceeding to the subsequent headline.",
                            "Advancing to the next headline.",
                            "Shifting focus to the subsequent headline.",
                            "Moving forward to the next headline.",
                            "Progressing to the subsequent headline."
                        ]

                        # Randomly choose a phrase
                        random_phrase = random.choice(phrases)
                        speak(random_phrase)
            else:
                speak("Failed to fetch news headlines.")
def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    print("URL:", url)  # Print the URL for debugging
    response = requests.get(url)
    data = response.json()
    print("Response:", data)  # Print the response for debugging
    return data
def display_weather(weather_data):
     if weather_data["cod"] == 200:
         speak(f"Weather in {weather_data['name']}:")
         speak(f"Description: {weather_data['weather'][0]['description']}")
         speak(f"Temperature: {weather_data['main']['temp']}°C")
         speak(f"Humidity: {weather_data['main']['humidity']}%")
         speak(f"Wind Speed: {weather_data['wind']['speed']} m/s")
         print(f"Weather in {weather_data['name']}:")
         print(f"Description: {weather_data['weather'][0]['description']}")
         print(f"Temperature: {weather_data['main']['temp']}°C")
         print(f"Humidity: {weather_data['main']['humidity']}%")
         print(f"Wind Speed: {weather_data['wind']['speed']} m/s")

     else:
         print("City not found. Please check the city name and try again.")
         speak("City not found. Please check the city name and try again.")
def jarvis_sleep():
    global is_sleeping
    is_sleeping = True
    speak("Going to sleep, Sir.")
    print("Jarvis is now sleeping.")
def jarvis_wake():
    global is_sleeping
    is_sleeping = False
    speak("Welcome back, Sir!")
    print("Jarvis is now awake.")
def OpenApps():
    if "open notepad" in query:
        path = "C:\\Windows\\system32\\notepad.exe"
        os.startfile(path)
    elif "chrome" in query:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    elif 'chat gpt' in query:
        open_chatgpt()
    elif "Facebook" in query or "facebook" in query:
        webbrowser.open("https://www.facebook.com")
    elif "Microsoft" in query:
        open_microsoft()
    elif 'gmail' in query:
        open_gmail()
    elif 'google' in query or 'Google' in query:
        webbrowser.open("https://www.google.com")
def CloseApps():
    if 'youtube' in query or 'google' in query or ' chat GPT' in query or 'google maps' in query or 'facebook' in query:
        os.system("TASKKILL/F /im msedge.exe")
    elif 'notepad' in query:
        os.system("TASKKILL/F /im notepad.exe")
    elif "open Facebook" in query or "open facebook" in query:
        webbrowser.open("https://www.facebook.com")
def SpeedTest():
    import speedtest

    speak("Checking speed....")
    speed = speedtest.Speedtest()
    downloading =  speed.download()
    correctDown = int(downloading/800000)
    uploading = speed.upload()
    correctUpload = int(uploading/800000)

    if 'uploading' in query:
        speak(f"The Uploading Speed Is {correctDown} mbp s")
    elif 'downloading' in query:
        speak(f"The Downloadiing Speed is {correctDown} mbp s")
    else:
        speak(f"The Downloading Speed is {correctDown} mb per s and The Uploading Speed is {correctUpload} mb per s")
def screenshot():
    speak("Ok sir, what should i name the file?")
    path = take_Command()
    path1name = path + ".png"
    path1 = "C:\\Users\\vilas\\Desktop\\Jarvis IMP files\\"+ path1name
    kk = pyautogui.screenshot()
    kk.save(path1)
    os.startfile("C:\\Users\\vilas\\Desktop\\Jarvis IMP files\\")
    speak("Here is your screenshot")
def run_system_diagnosis():
    

    cpu_usage = psutil.cpu_percent()  # Get CPU usage percentage
    memory_usage = psutil.virtual_memory().percent  # Get memory usage percentage
    battery = psutil.sensors_battery()  # Get battery information

    # Inform user about system status
    speak("Running system diagnosis...")
    speak(f"CPU Usage: {cpu_usage}%")
    speak(f"Memory Usage: {memory_usage}%")

    if battery is not None:
        battery_percent = battery.percent
        if battery.power_plugged:
            speak(f"Battery is {battery_percent}% charged (Plugged in)")
        else:
            speak(f"Battery is {battery_percent}% charged (Not plugged in)")
    else:
        speak("Battery information not available.")





if __name__ == "__main__":
    wish_me()
    is_sleeping = False
    while True:
        if not is_sleeping:
            query = take_Command()
            if not query:  # Check if query is an empty string
                continue  # Skip the rest of the loop and restart from the beginnin
            elif "hello" in query:
                speak("Hello Sir, Welcome Back!")
            elif "time" in query:
                from datetime import datetime

                time = datetime.now().strftime("%H:%M")
                speak(f"The Time Now Is : {time}")
            elif "bye" in query:
                speak("Nice to meet you sir, Have a nice day!")
            elif 'run system diagnosis' in query:
                run_system_diagnosis()
            elif 'open youtube' in query:
                speak("Which video do you want to watch on YouTube?")
                query = query.replace("jarvis", "")
                query = query.replace("youtube", "")
                query = query.replace("search", "")
                video_query = take_Command()
                open_youtube_video(video_query)
            elif 'read news' in query:
                read_news()
            elif 'weather' in query or 'temperature' in query:
                query = query.replace("what", "")
                query = query.replace("is", "")
                query = query.replace("the", "")
                query = query.replace("in", "")
                query = query.replace("jarvis", "")
                query = query.replace("weather", "")
                query = query.replace("temperature", "")
                city = query
                api_key = "0c18f5f50a41823f36267fde678f2ca2" # Replace "your_api_key_here" with your actual API key
                weather_data = get_weather(api_key, city)
                display_weather(weather_data)
            elif "open" in query:
                OpenApps()
            elif 'jarvis sleep' in query or 'sleep' in query:
                jarvis_sleep()
            elif 'jarvis wake up' in query:
                jarvis_wake()
            elif 'launch' in query:
                speak("OK sir, Launching...")
                query = query.replace("jarvis", "")
                query = query.replace("website", "")
                query = query.replace(" ", "")
                query = query.replace("launch", "")
                web1 = query.replace("open", "")
                web2 = 'https://www.' + web1 + '.com'
                webbrowser.open(web2)
                speak("Launched")
            elif 'screenshot' in query:
                screenshot()
            elif "what's the time" in query or "what is the time" in query or "what is the time now" in query or "whats is time" in query or "tell me the time" in query or "what is the time right now" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
            elif "wikipedia" in query:
                speak("Searching Wikipedia... Please wait.")
                query = query.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak("Wikipedia says")
                    print(results)
                    speak(results)

                    speak("Do you want more information?")
                    response = take_Command().lower()
                    if "yes" in response:
                        full_article = wikipedia.page(query).content
                        article_length = len(full_article)
                        current_index = 0
                        speak("Starting the full article.")
                        while current_index < article_length:
                            next_chunk = full_article[current_index:current_index + 500]
                            speak(next_chunk)
                            current_index += 500

                            speak("Do you want me to continue?")

                            if response != "yes":
                                speak("Alright, stopping.")
                                break
                except wikipedia.exceptions.DisambiguationError as e:
                    speak(f"There are multiple options for this query. Please be more specific: {', '.join(e.options)}")
                except wikipedia.exceptions.PageError:
                    speak("Sorry, I couldn't find any information on that topic.")
                except Exception as e:
                    speak("An error occurred while processing your request.")
                    print(e)
            elif "close website" in query:
                CloseApps()
            elif "close notepad" in query:
                CloseApps()
            elif "repeat my words" in query:
                speak("Speak Sir!")
                jj = take_Command()
                speak("You Said :" + jj)
            elif "my location" in query:
                webbrowser.open("https://www.google.co.in/maps/place/Acme+Ozone+Phase+2/@19.2327152,72.9717729,18.35z")
                speak("sir, your current location is Acme Ozone,  Thane, Maharashtra, India")
            elif 'alarm' in query:
                speak("Enter Time please :")
                time = input("Enter the time :")

                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")

                    if now == time:
                        speak("Time has came sir!")
                        speak("Alarm closed!")
                    elif now>time:
                        speak("Time has came sir!")
                        speak("Alarm closed!")
            elif 'remember that' in query:
                rememberMsg = query.replace("jarvis", "")
                rememberMsg = rememberMsg.replace("remember that", "")
                rememberMsg = rememberMsg.replace("i","you")
                speak("You told me to remind you that: " + rememberMsg)
                with open('data.txt', 'w') as remember_file:
                    remember_file.write(rememberMsg)
            elif 'what do you remember' in query:
                try:
                    with open('data.txt', 'r') as remember_file:
                        remembered_text = remember_file.read()
                        speak("You told me that: " + remembered_text)
                except FileNotFoundError:
                    speak("I don't remember anything.")
            elif 'clear data' in query:
                with open('data.txt', 'w') as remember_file:
                    remember_file.write('')
                speak("Memory cleared.")
            elif 'search on google' in query or "google search" in query:
                import wikipedia as googleScrap
                query = query.replace('jarvis', "")
                query = query.replace('google', "")
                query = query.replace('search', "")
                query = query.replace('on', "")
                speak("This is what I found on Google")

                try:
                    pywhatkit.search(query)
                    result = googleScrap.summary(query, 3)
                    print(result)
                    speak(result)
                except:
                    speak("No Speakable Data avaliable")
            elif 'internet speed' in query:
                SpeedTest()
            elif 'downloading speed' in query:
                SpeedTest()
            elif 'uploading speed' in query:
                SpeedTest()
            elif 'how to' in query:
                speak("Searching the web please wait")
                op = query.replace("jarvis", "")
                op = query.replace("tell me", "")
                max_result = 1
                how_to_func = search_wikihow(op,max_result)
                assert len(how_to_func) == 1
                how_to_func[0].print()
                speak(how_to_func[0].summary)
            elif any(word in query for word in ['exit', 'quit', 'break']):
                speak("Thank you for using Jarvis, Sir.")
                break
            elif "hello" in query:
                speak("Hello! How can I help you today?")
            elif "how are you" in query:
               speak("I'm doing well, thank you! What about you?")
            elif "what is your name" in query:
                speak("I'm your virtual assistant. You can call me Jarvis!")
            elif "bye" in query:

                speak("Goodbye! Have a great day.")
                break
            else:
                    speak(response)
        else:
            wake_up_command = take_Command()
            if 'jarvis wake up' in wake_up_command or 'wake up' in wake_up_command:
                jarvis_wake()
            else:
                print("Jarvis is currently sleeping. Say 'Jarvis wake up' to wake him up.")
