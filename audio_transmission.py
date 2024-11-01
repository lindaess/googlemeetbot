# audio_transmission.py

import requests

def send_audio(file_path, api_url):
    try:
        with open(file_path, 'rb') as f:
            response = requests.post(api_url, files={'file': f})
            if response.ok:
                print("File sent successfully.")
            else:
                print(f"Failed to send file: {response.status_code}")
    except Exception as e:
        print(f"Error sending file: {e}")

if __name__ == "__main__":
    api_url = "https://your_api_endpoint.com/upload"  # Replace with actual API endpoint
    send_audio("test_audio.wav", api_url)
