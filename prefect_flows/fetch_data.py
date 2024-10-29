import os
import json
import requests

from prefect import task, flow

@task
def fetch_query_cities():
    source_url = 'https://github.com/lutangar/cities.json/blob/master/cities.json'
    response = requests.get(source_url)
    json_object = json.load(response.json())
    return json_object

@task
def fetch_data_from_rapidapi(querystring):
    rapid_api_key = os.getenv("RAPID_API")  

    # Set the endpoint and query parameters
    weather_url = "https://weatherapi-com.p.rapidapi.com/current.json"
    print(querystring)

    # Define the headers with the RapidAPI host and key
    headers = {
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com",
        "x-rapidapi-key": rapid_api_key
    }
    
    #response = requests.get(weather_url, headers=headers, params=querystring)
    #return response.json()

# @task
# def store_data_as_csv():

@flow
def my_pipeline():
    query_cities = fetch_query_cities()
    for queries in query_cities:
        data = fetch_data_from_rapidapi(queries)
        break
    print(data)
