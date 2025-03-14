import librosa
import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wav
from speakListen import speak

# Function to record voice and save it as a WAV file
def record_audio(duration=3, sample_rate=22050):
    print("Listening for emotion...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    wav.write("emotion.wav", sample_rate, audio_data)
    return "emotion.wav"

# Function to extract features from audio
def extract_features(audio_file):
    y, sr = librosa.load(audio_file)
    mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13).T, axis=0)
    return mfccs

# Dummy function for emotion classification (Replace with AI model later)
def classify_emotion(audio_file):
    features = extract_features(audio_file)
    
    # TODO: Replace this with a trained AI model
    emotions = ["happy", "sad", "angry", "neutral"]
    detected_emotion = np.random.choice(emotions)  # Temporary random choice
    
    return detected_emotion

# Function to analyze and respond based on emotion
def analyze_voice_emotion():
    audio_file = record_audio()
    emotion = classify_emotion(audio_file)
    
    print(f"Detected Emotion: {emotion}")
    if emotion == "happy":
        speak("You sound happy! That's awesome! How’s your day going?")
    elif emotion == "sad":
        speak("You sound a bit down. Do you want to talk about it?")
    elif emotion == "angry":
        speak("You seem frustrated. Want to do some breathing exercises?")
    else:
        speak("I’m here for you. Let’s talk!")
    
    return emotion
