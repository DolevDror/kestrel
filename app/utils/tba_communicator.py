import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Function to retrive the tba key from its enviorment variable
def get_api_key():
    return os.getenv("TBA_KEY")

async def tba_request(api_url):
    request = None
    full_url = f"https://www.thebluealliance.com/api/v3/{api_url}" # The base url for all tba requests
    request_headers = {"X-TBA-Auth-Key": get_api_key()} # Set the key in the header
    print(f"starting api request to {full_url}")
    try:
        request = requests.get(full_url, headers=request_headers)
        print(f"finished api request from {full_url}")
    except requests.exceptions.ConnectionError:
        print(f"ERROR: No internet")
        return None

    if request.status_code == 200: # Status code 200 is sucessfull 
        return request.json()
    