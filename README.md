# Google Meet Automation Bot
This project is a Python bot that  automates the process of joining a Google Meet session, recording audio during the meeting, and transmitting the recorded audio to a specified API. It uses Selenium for browser automation and integrates audio recording and speech-to-text functionalities.



##Features
- Automatically logs into Google using specified credentials.
- Joins a Google Meet meeting using a provided link.
- Mutes the microphone and camera upon joining.
- Records audio during the meeting.
- Transmits the recorded audio file to a specified API endpoint.
## Prerequisites

- Python 3.8 or higher
- Chrome browser
- OpenAI Api Key
- A Gmail account
- A Google Meet link
-Selenium
- Requests

## Installation

1. Clone the repository:

   ```bash
   

2. Make python environment:

   ```bash
   python3 -m venv env

3. Activate environment(Ubuntu):

   ```bash
   source env/bin/activate

3. Activate environment(Windows):

   ```bash
   env/scripts/activate

4. Install requirements:

   ```bash
   pip install -r requirements.txt

5.  Export credentials to environments:

   ```bash
   
   export email_id="youremail@gmail.com"
   
   export email_password="you password"
   ```


6. Run Script:

   ```bash
   python3 join_google_meet.py


https://github.com/ExistentialAudio/BlackHole?tab=readme-ov-file#features
brew install blackhole-2ch
https://github.com/ExistentialAudio/BlackHole/wiki/Multi-Output-Device

brew install ffmpeg

   