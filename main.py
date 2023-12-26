import os
import requests
import streamlit as st
import json

def get_weather(api_key, city_name, temperature_unit='metric'):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city_name}&units={temperature_unit}"

    if temperature_unit == 'metric':
        temperature_unit = '°C'
    else:
        temperature_unit = '°F'

    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        weather_data = response.json()

        st.write("The weather in " + city_name + " is:")
        st.write("Weather:", weather_data["weather"][0]["description"])
        st.write("Temperature:", weather_data["main"]["temp"], f"{temperature_unit.upper()}")
        st.write("Wind Speed:", weather_data["wind"]["speed"], "m/s")
        st.write("Humidity:", weather_data["main"]["humidity"], "%")
        st.write("\n")

    except requests.exceptions.HTTPError as errh:
        st.write(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        st.write(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        st.write(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        st.write(f"Request Exception: {err}")

def get_news(api_key):
    url = 'https://newsapi.org/v2/top-headlines?' 'country=us&' f'apiKey={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        news_data = response.json()

        articles = news_data['articles']
        st.write("Top 20 Headlines:")
        for index, article in enumerate(articles, start=1):
            st.write('------------------------------------------')
            st.write('\n' + f"Article {index}")
            st.write('\n' + f"Author {index}")
            st.write(article['author'])
            st.write('\n' + f"Title {index}")
            st.write(article['title'])
            st.write('\n' + f"Description {index}")
            st.write(article['description'])
            st.write('\n' + f"Published on {index}")
            st.write(article['publishedAt'])
            st.write('\n' + f"Content {index}")
            st.write(article['content'])
            st.write('\n' + f"URL {index}")
            st.write(article['url'])
            st.write('------------------------------------------')

    except requests.exceptions.HTTPError as errh:
        st.write(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        st.write(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        st.write(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        st.write(f"Request Exception: {err}")

def main():
    # Replace with your API keys
    api_key_weather = "api_key_weather"
    api_key_news = "api_key_news"

    if not api_key_weather or not api_key_news:
        st.write("Please provide API keys.")
        return

    st.title("Weather and News Tracker🌦️📰")
    
    city_name = st.text_input("Enter city name:")
    temperature_unit = st.text_input("Enter temperature unit (default is Celsius, enter 'imperial' for Fahrenheit): ")

    if temperature_unit.lower() not in ['metric', 'imperial']:
        temperature_unit = 'metric'

    if st.button("Get Weather and News"):
        get_weather(api_key_weather, city_name, temperature_unit)
        get_news(api_key_news)

if __name__ == "__main__":
    main()