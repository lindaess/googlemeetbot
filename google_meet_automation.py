# google_meet_automation.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def join_meet_link(meet_url):
    options = webdriver.ChromeOptions()
    options.add_argument("--use-fake-ui-for-media-stream")  # Allows use of mic without prompts
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(meet_url)
        time.sleep(5)  # Wait for page to load
        
        # Attempt to find and click the "Join now" button
        join_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Join now')]")
        if join_button:
            join_button.click()
            print("Joined Google Meet successfully.")
        else:
            print("Join button not found.")
        
        # Keep the meeting session open for testing purposes
        time.sleep(60)
    except Exception as e:
        print(f"Error during meeting join: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    meet_url = "https://meet.google.com/zun-rvun-qrb"  # Replace with actual Google Meet link
    join_meet_link(meet_url)
