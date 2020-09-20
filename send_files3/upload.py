import os
import base64
import requests
from datetime import date

API_URL = os.environ['API_URL']
API_KEY = os.environ['API_KEY']

def upload_to_aws(local_file):
    with open("image.jpg", 'rb') as file:
        encoded_data = base64.b64encode(file.read())
    response = requests.put(API_URL,data=encoded_data ,headers={"x-api-key": API_KEY})
    print(date.today())
    print(response)
