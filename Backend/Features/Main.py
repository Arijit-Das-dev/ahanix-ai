import os
from groq import Groq
from datetime import datetime
import requests
import speech_recognition as sr
import streamlit as st
import pyaudio
import warnings
import random
from dotenv import load_dotenv
from Frontend.F_Main import style3_MAIN, animation
from DB.wake_db import insert_wake
from DB.weather_db import insert_weather
import base64
from DB.MainDB import insert_into_user, insert_into_assistant
import uuid
import io
import edge_tts
import asyncio
import time as t



# ---------- Session variables (TOP) ----------
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

user_id = st.session_state.user_id

style3_MAIN()
animation()

# IGNORE WARNING
warnings.filterwarnings("ignore")

# CORE ENGINE 
class CoreEngine:

    def __init__(self):
        self.is_speaking = False

    def speak(self, text):

        async def generate_audio():
            communicate = edge_tts.Communicate(
                text=text,
                voice="en-US-GuyNeural",
                rate="+3%",
                pitch="+1Hz"
            )

            audio_bytes = b""
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    audio_bytes += chunk["data"]

            return audio_bytes

        try:
            self.is_speaking = True   # 🔴 LOCK MIC

            audio_bytes = asyncio.run(generate_audio())
            audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

            audio_html = f"""
            <audio autoplay>
                <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
            </audio>
            """

            st.markdown(audio_html, unsafe_allow_html=True)

            # ⏳ WAIT till audio finishes (important!)
            t.sleep(len(text) * 0.06)

        except Exception as e:
            st.error(f"Edge TTS Error: {str(e)}")

        finally:
            self.is_speaking = False   # 🟢 UNLOCK MIC

    # -> ----------- PASSIVE WAKE LISTENING ------------- <-
    def listen_wake_word(self):

        r = sr.Recognizer()

        # Optimized settings for wake word detection
        r.energy_threshold = 300  # Lower = more sensitive
        r.pause_threshold = 0.5   # Shorter pause detection
        r.dynamic_energy_threshold = True  # Auto-adjust to environment
        
        wake_words = ["jarvis", "jarves", "jar vis", "javis"]  # Common mishearings
        
        while True:
            try:
                with sr.Microphone() as source:
                    print("🎧 Listening for wake word...")
                    
                    # Better ambient noise adjustment => [Noise cancelation]
                    r.adjust_for_ambient_noise(source, duration=1)
                    
                    # Shorter phrase limit for wake word
                    audio = r.listen(source, timeout=10, phrase_time_limit=5)

                # Recognize speech
                said = r.recognize_google(audio, language='en-in').lower()
                print(f"Detected: '{said}'")
                st.write(f"Heard: {said}")

                # Check wake word with fuzzy matching
                if any(wake_word in said for wake_word in wake_words):
                    print("🚀 Wake word detected: JARVIS!!!")
                    return True

            except sr.WaitTimeoutError:
                print("⏳ Listening...")
                continue

            except sr.UnknownValueError:
                print("❌ Could not understand — retrying...")
                continue

            except sr.RequestError as e:
                st.error(f"⚠️ Network error: {e}")
                continue

            except Exception as e:
                print(f"⚠️ Error: {e}")
                continue

    # -> ----------- ACTIVE COMMAND LISTENING ------------ <-
    def take_command(self):

        if self.is_speaking:
            return "none"   # 🚫 Ignore input while speaking

        r = sr.Recognizer()
        r.energy_threshold = 200
        r.pause_threshold = 1.0
        r.dynamic_energy_threshold = True

        try:
            with sr.Microphone() as source:
                st.write("🎧 Listening for command...")
                r.adjust_for_ambient_noise(source, duration=1.5)

                audio = r.listen(
                    source,
                    timeout=30,
                    phrase_time_limit=25
                )

            query = r.recognize_google(audio, language='en-in').lower()

            insert_into_user(user_id=user_id, query_user=query)

            st.success(f"✅ You said: {query}")
            return query

        except:
            return "none"

class Jarvis(CoreEngine):

    def __init__(self):

        load_dotenv()
        API_KEY = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=API_KEY)
        self.chat_history = [] # Chat history

    def ask_llama(self, prompt):

        self.chat_history.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=self.chat_history  # send full chat history
        )

        bot_reply = response.choices[0].message.content

        # Store assistant reply too
        self.chat_history.append({

            "role": "assistant", 
            "content": bot_reply
        })

        return bot_reply

    def JarvisRun(self, user2):


            if "weather" in user2:

                latitude = 22.57
                longitude = 88.36

                url = (
                    f"https://api.open-meteo.com/v1/forecast?"
                    f"latitude={latitude}&longitude={longitude}"
                    f"&current_weather=true"
                    f"&hourly=relativehumidity_2m,pressure_msl,cloudcover"
                )

                try:
                    response = requests.get(url)
                    data = response.json()

                    # Current weather
                    temperature = data['current_weather']['temperature']
                    windspeed = data['current_weather']['windspeed']
                    winddirection = data['current_weather']['winddirection']
                    weather_code = data['current_weather']['weathercode']

                    # Hourly extra parameters (take index 0 = current hour)
                    humidity = data['hourly']['relativehumidity_2m'][0]
                    pressure = data['hourly']['pressure_msl'][0]
                    cloud_cover = data['hourly']['cloudcover'][0]
                    insert_weather(temperature, windspeed, winddirection, weather_code, humidity, pressure, cloud_cover)

                except Exception as e:

                    print(f"Error : {e}")
                    j.speak(f"{e}")
                
                j.speak(f"Today's temperature is {temperature} degree celsius ")
                j.speak(f"windspeed is {windspeed} kilometre per hour")

            elif "exit" in user2:

                self.speak('''Okay sir, i am going to sleep now, if you need anything, just wake me up by saying "hey jarvis" ''')
                return "exit"
            
            else:
                try:
                    root_dir = os.path.abspath(
                        os.path.join(os.path.dirname(__file__), "..", "..")
                    )
                    prompt_path = os.path.join(root_dir, "Prompt", "mainPrompt.txt")

                    with open(prompt_path, "r", encoding="utf-8") as f:
                        system_prompt = f.read()

                    final_prompt = f"{system_prompt}\nUser: {user2}\nAssistant:"
                    
                    reply = self.ask_llama(final_prompt)
                    print("Assistant:", reply)
                    self.speak(reply)
                    insert_into_assistant(user_id=user_id, ai_answer=reply)

                except Exception as e:

                    print("LLM Error:", e)
                    self.speak("I did not hear that properly, tell that again")

# Accessing all classes by creating [objects -> CoreEngine -> jarvis]
j = Jarvis()

# Welcome message ->
def greet():

    latitude = 22.57
    longitude = 88.36

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    try:
       
       response = requests.get(url)
       data = response.json()

       temperature = data['current_weather']['temperature']
       windspeed = data['current_weather']['windspeed']

    except Exception as e:

        print(f"Error : {e}")
        j.speak(f"{e}")

    # TIME CONFIGURATION
    hour = datetime.now().hour

    if 5 <= hour < 12:
        j.speak("Good morning sir. Welcome to a brand-new day.")
        t.sleep(1.2)
    elif 12 <= hour < 17:
        j.speak("Good afternoon sir. I hope your day is going smoothly.")
        t.sleep(1.2)
    elif 17 <= hour < 21:
        j.speak("Good evening sir, welcome back.")
        t.sleep(1.2)
    else:
        j.speak("Welcome back sir!")
        t.sleep(1.2)

    j.speak(f"Today's temperature is {temperature} degree celsius ")
    t.sleep(1.5)
    j.speak(f"windspeed is {windspeed} kilometre per hour")
    t.sleep(1.3)

    j.speak("Tell me how can I assist you?")
    
if __name__ == "__main__":
    
    greet()

    while True:
        # Listen only for wake word
        wake_word = j.listen_wake_word()

        if wake_word:
            # Insert wake word in DB (if needed)
            insert_wake(wake_word)

            
            j.speak("Yes sir")

            # Run main Jarvis conversation
            query = j.take_command()

            if query != "none":
                result = j.JarvisRun(query)

                if result == "exit":
            # After finishing, loop continues to listen again
                    break

        t.sleep(0.2)