# import required modules
import os
import tempfile
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import sounddevice as sd
from scipy.io.wavfile import write
import whisper

def transcribe_audio_whisper(filename):
    model = whisper.load_model("base")  # You can choose other models like "small", "medium", or "large"
    result = model.transcribe(filename)
    text = result["text"]
    print("Transcription:", text)
    # Save transcription to a text file
    with open("output.txt", "w") as f:
        f.write(text)

    print(f"Transcription saved to output.txt")
    return text

# Function to record audio
def record_audio(filename, duration=20, sample_rate=44100):
    print("Recording audio...")
    print(sd.query_devices())
    sd.default.device = 0
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()  # Block until recording is finished
    write(filename, sample_rate, audio)
    print(f"Recorded audio saved as {filename}")
    # Save the audio data as raw PCM
    with open(filename + ".pcm", 'wb') as f:
        f.write(audio.tobytes())

# Function to send transcription to API
def send_transcription_to_api(api_url, meeting_id, transcription_text):
    print(f"Sending transcription to API: {api_url}")
    payload = {
        "meetingId": meeting_id,  # Set this to the actual meeting ID
        "type": "google",
        "transcript": transcription_text
    }
    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            print("Transcription sent successfully.")
            print("API Response:", response.json())
        else:
            print(f"Failed to send transcription: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"An error occurred while sending transcription to API: {e}")

class JoinGoogleMeet:
    def __init__(self, meet_link):
        self.mail_address = os.environ.get('email_id')
        self.password = os.environ.get('email_password')
        self.meet_link = meet_link
        print(f"Email: {self.mail_address}")

        # create chrome instance
        opt = Options()
        opt.add_argument('--disable-blink-features=AutomationControlled')
        opt.add_argument('--start-maximized')
        opt.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 0,
            "profile.default_content_setting_values.notifications": 1
        })
        self.driver = webdriver.Chrome(options=opt)
        print("Chrome driver initialized")

    def Glogin(self):
        print("Navigating to Google login page")
        self.driver.get('https://accounts.google.com/signin')
        self.driver.implicitly_wait(5)
        
        print("Entering email")
        self.driver.find_element(By.ID, "identifierId").send_keys(self.mail_address)
        self.driver.find_element(By.ID, "identifierNext").click()
        self.driver.implicitly_wait(10)
        
        print("Entering password")
        self.driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(self.password)
        self.driver.find_element(By.ID, "passwordNext").click()
        self.driver.implicitly_wait(10)
        print("Gmail login activity: Done")

    def click_ask_to_join(self):
        try:
            ask_to_join_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(translate(., 'JOIN', 'join'), 'join')]"))
            )
            ask_to_join_button.click()
            print("Clicked button containing 'join' successfully.")
        except TimeoutException:
            print("Timed out waiting for a button with 'join' to be clickable.")
        except NoSuchElementException:
            print("Button with 'join' not found.")

    def navigate_to_meet(self, meet_link):
        print(f"Navigating to Google Meet link: {meet_link}")
        self.driver.get(meet_link)
        time.sleep(2)

def main():
    temp_dir = tempfile.mkdtemp()
    audio_path = os.path.join(temp_dir, "output_audio.wav")
    meet_link = 'https://meet.google.com/zun-rvun-qrb'   # Replace with actual Google Meet link
    api_url = 'https://ai.mypop.ai/api/transcript'  # Replace with your API endpoint
    meeting_id = "googlemeetingID"  # Replace this with the actual Google Meeting ID
    duration = 20

    print("Starting Google Meet bot")
    obj = JoinGoogleMeet(meet_link)
    obj.Glogin()
    obj.navigate_to_meet(meet_link)
    obj.click_ask_to_join()
    time.sleep(5)

    # Record and transcribe audio
    record_audio(audio_path, duration=duration)
    transcription_text = transcribe_audio_whisper(audio_path)
    
    # Send transcription to API
    send_transcription_to_api(api_url, meeting_id, transcription_text)

    input("Press Enter to continue and close the browser...")
    obj.driver.quit()

if __name__ == "__main__":
    main()
