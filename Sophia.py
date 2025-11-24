import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import datetime
import pytz # For Timezone handling

# --- Initialization ---

# Initialize the recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set female voice (optional)
voices = engine.getProperty('voices')
# Use the second voice if available (often female), otherwise default to the first
try:
    engine.setProperty('voice', voices[1].id) 
except IndexError:
    engine.setProperty('voice', voices[0].id)

# --- Core Functions ---

def talk(text):
    """Converts text to speech and prints it to the console."""
    print("sophia:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listens to user's voice, recognizes the command using Google API, and processes it."""
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            
            # Using Google's Speech Recognition API (Requires internet)
            command = listener.recognize_google(voice)
            
            command = command.lower()
            if 'sophia' in command:
                command = command.replace('sophia', '').strip()
            print("You said:", command)
            
    except sr.UnknownValueError:
        # User spoke but the voice wasn't understood
        print("Sorry, I didn't understand that.")
        talk("Sorry, I didn't catch that. Could you please repeat?")
        command = "" # Return empty string to prevent executing partial commands
    except sr.RequestError:
        # Network error
        print("Network error. Check your internet connection.")
        talk("I seem to have a network problem. Please check your internet connection.")
        command = ""
    except Exception as e:
        # Catch other unexpected errors
        print(f"An unexpected error occurred: {e}")
        command = ""
        
    return command

def run_sophia():
    """Processes the recognized command and responds accordingly."""
    command = take_command()
    if not command:
        return # Exit if command is empty/unrecognized

    # --- 1. Play Music ---
    if 'play' in command:
        song = command.replace('play', '').strip()
        talk("Playing " + song)
        pywhatkit.playonyt(song)
        
    # --- 2. Time (Timezone Aware for India/Kolkata) ---
    elif 'time' in command:
        # Define the Indian Standard Timezone (IST)
        IST = pytz.timezone('Asia/Kolkata')
        # Get the current time in IST
        now = datetime.datetime.now(IST)
        time = now.strftime('%I:%M %p')
        talk(f"The current time in India is {time}")
        
    # --- 3. Date ---
    elif 'date' in command:
        today = datetime.date.today().strftime('%A, %B %d, %Y')
        talk(f"Today is {today}")
        
    # --- 4. Wikipedia Search (Who Is) ---
    elif 'who is' in command or 'who the heck is' in command:
        person = command.replace('who the heck is', '').replace('who is', '').strip()
        try:
            # Get only the first sentence for a brief summary
            info = wikipedia.summary(person, sentences=1, auto_suggest=False, redirect=True) 
            print(info)
            talk(info)
        except wikipedia.exceptions.PageError:
            talk(f"Sorry, I couldn't find any information on {person}")
        except wikipedia.exceptions.DisambiguationError:
            talk(f"The term {person} is ambiguous. Please be more specific.")
            
    # --- 5. General Fact/Search (Opens browser with search results) ---
    elif 'what is' in command or 'tell me about' in command or 'search for' in command:
        # Create a clean query string
        query = command.replace('what is', '').replace('tell me about', '').replace('search for', '').strip()
        
        if query:
            talk(f"Searching the web for {query}")
            # pywhatkit.search will open a browser window with the search results
            pywhatkit.search(query)
        else:
            talk("What would you like me to search for?")
            
    # --- 6. Jokes & Small Talk ---
    elif 'are you single' in command or 'married' in command:
        talk("I am in a relationship with Wi-Fi.")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
    # --- 7. Catch-all for unknown commands ---
    else:
        talk("I'm sorry, I am not programmed to handle that specific command yet.")


# --- Main Loop ---

# Run Sophia continuously
while True:
    run_sophia()
