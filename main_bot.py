# main_bot.py

from oauth_authentication import get_credentials
from google_meet_automation import join_meet_link
from audio_recording import record_audio
from audio_transmission import send_audio

def main():
    # Load OAuth credentials
    credentials = get_credentials()
    if not credentials:
        print("Error loading credentials. Exiting.")
        return
    
    # Join Google Meet
    meet_url = "https://meet.google.com/zun-rvun-qrb"  # Replace with actual Google Meet link
    join_meet_link(meet_url)
    
    # Record Audio
    audio_file = "meeting_audio.wav"
    duration = 60  # Duration for recording audio in seconds
    record_audio(audio_file, duration)
    
    # Send Audio File to API
    api_url = "https://your_api_endpoint.com/upload"  # Replace with actual API endpoint
    send_audio(audio_file, api_url)

if __name__ == "__main__":
    main()
