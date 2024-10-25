import os
import requests

from prefect import task, flow

@task
def fetch_data_from_rapidapi():
    api_key = os.getenv("RAPID_API")  

    # Set the endpoint and query parameters
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": "53.1,-0.13"} # Coordinates London just an example

    # Define the headers with the RapidAPI host and key
    headers = {
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com",
        "x-rapidapi-key": api_key
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

@flow
def my_pipeline():
    data = fetch_data_from_rapidapi()
    print(data)
