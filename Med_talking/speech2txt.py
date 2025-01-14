import speech_recognition as sr
import sounddevice as sd
import numpy as np
import os
import scipy.io.wavfile as wav

def listen_and_transcribe(duration=5, sample_rate=16000):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished

    # Save the audio data as a WAV file
    temp_wav_path = 'temp_audio.wav'
    wav.write(temp_wav_path, sample_rate, audio_data.flatten())

    # Load the audio file
    with sr.AudioFile(temp_wav_path) as source:
        # Record the audio data from the file
        audio_data = recognizer.record(source)

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            # Google Speech Recognition could not understand the audio
            text = "Sorry, I could not understand the audio."
        except sr.RequestError as e:
            # Google Speech Recognition request failed
            text = f"Sorry, there was an error with the request: {e}"

    # Remove the temporary WAV file
    os.remove(temp_wav_path)
    print("processing")

    

    return text
    
    

text = listen_and_transcribe(duration=5, sample_rate=16000)
print(text)


