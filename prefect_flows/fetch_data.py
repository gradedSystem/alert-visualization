import os
import requests

from prefect import task, flow

@task
def fetch_data_from_rapidapi():
    api_key = os.getenv("RAPID_API_KEY")  # Securely get the API key from the environment
    url = "https://example-rapidapi-endpoint"
    
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "example-rapidapi-host"
    }
    
    response = requests.get(url, headers=headers)
    return response.json()

@flow
def my_pipeline():
    data = fetch_data_from_rapidapi()
    print(data)
