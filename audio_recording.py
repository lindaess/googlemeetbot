# audio_recording.py

import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename, duration=10, sample_rate=44100):
    print("Recording audio...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()  # Block until recording is finished
    write(filename, sample_rate, audio)
    print(f"Recorded audio saved as {filename}")

if __name__ == "__main__":
    record_audio("test_audio.wav", duration=5)
