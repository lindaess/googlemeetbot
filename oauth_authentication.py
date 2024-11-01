# oauth_authentication.py

from google.oauth2 import service_account

def get_credentials():
    try:
        creds = service_account.Credentials.from_service_account_file("credentials.json")
        print("OAuth credentials loaded successfully.")
        return creds
    except Exception as e:
        print(f"Error loading credentials: {e}")
        return None

if __name__ == "__main__":
    credentials = get_credentials()
