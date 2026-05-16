import speech_recognition as sr
import os
import time
import asyncio
import edge_tts
import pygame
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Configuration
WAKE_WORD = "assistant"
LLM_MODEL = "llama-3.1-8b-instant"
STT_MODEL = "whisper-large-v3"
TEMP_AUDIO_FILE = "response.mp3"

# Initialize Pygame mixer for audio playback
pygame.mixer.init()

async def text_to_speech(text):
    """Converts text to speech using edge-tts and plays it."""
    start_time = time.time()
    communicate = edge_tts.Communicate(text, "en-US-GuyNeural")
    await communicate.save(TEMP_AUDIO_FILE)
    tts_latency = time.time() - start_time
    
    pygame.mixer.music.load(TEMP_AUDIO_FILE)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    # Cleanup temp file
    pygame.mixer.music.unload()
    if os.path.exists(TEMP_AUDIO_FILE):
        os.remove(TEMP_AUDIO_FILE)
        
    return tts_latency

def get_llm_response(query):
    """Sends query to Groq LLM and returns the response."""
    start_time = time.time()
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful and concise voice assistant. Respond briefly."
            },
            {
                "role": "user",
                "content": query,
            }
        ],
        model=LLM_MODEL,
    )
    llm_latency = time.time() - start_time
    return chat_completion.choices[0].message.content, llm_latency

def transcribe_audio(audio_data):
    """Transcribes audio using Groq's Whisper model."""
    try:
        # Convert audio data to WAV format in memory
        wav_data = audio_data.get_wav_data()
        
        # Call Groq Whisper API
        transcription = client.audio.transcriptions.create(
            file=("speech.wav", wav_data),
            model=STT_MODEL,
            response_format="text",
        )
        return transcription.strip().lower()
    except Exception as e:
        print(f"STT Error: {e}")
        return ""

def listen_for_wake_word(recognizer, source):
    """Listens for the wake word using Whisper."""
    print(f"Listening for wake word '{WAKE_WORD}'...")
    audio = recognizer.listen(source)
    text = transcribe_audio(audio)
    if text:
        print(f"Heard: {text}")
        if WAKE_WORD in text:
            return True
    return False

def get_user_query(recognizer, source):
    """Captures user query after wake word is detected."""
    print("Listening for your query...")
    start_time = time.time()
    audio = recognizer.listen(source)
    
    start_transcribe = time.time()
    query = transcribe_audio(audio)
    stt_latency = time.time() - start_time # Includes listening and transcription
    
    if query:
        print(f"User Query: {query}")
        return query, stt_latency
    else:
        print("Could not understand audio.")
        return None, stt_latency

async def main():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        while True:
            if listen_for_wake_word(recognizer, source):
                print("Wake word detected!")
                
                query, stt_latency = get_user_query(recognizer, source)
                
                if query:
                    # Get LLM Response
                    response_text, llm_latency = get_llm_response(query)
                    print(f"AI Response: {response_text}")
                    
                    # Convert to Speech and Play
                    tts_latency = await text_to_speech(response_text)
                    
                    # Total Latency
                    total_latency = stt_latency + llm_latency + tts_latency
                    
                    print("\n--- Latency Report ---")
                    print(f"STT Latency: {stt_latency:.2f}s")
                    print(f"LLM Latency: {llm_latency:.2f}s")
                    print(f"TTS Latency: {tts_latency:.2f}s")
                    print(f"Total Latency: {total_latency:.2f}s")
                    print("----------------------\n")
                else:
                    print("No query detected.")

if __name__ == "__main__":
    if not os.getenv("GROQ_API_KEY"):
        print("Error: GROQ_API_KEY not found in .env file.")
    else:
        asyncio.run(main())
