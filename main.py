import requests
import streamlit as st

st.set_page_config(page_title="CityInsight", page_icon="🌆", layout="wide", initial_sidebar_state="expanded")

city_exists = False

def get_weather(api_key, city_name, temperature_unit='metric'):
    global city_exists
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': temperature_unit
    }

    if temperature_unit == 'metric':
        temperature_unit = '°C'
    else:
        temperature_unit = '°F'

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        st.write("The weather in " + city_name + " is:")
        st.write("Weather:", weather_data["weather"][0]["description"])
        st.write("Temperature:", weather_data["main"]["temp"], f"{temperature_unit.upper()}")
        st.write("Wind Speed:", weather_data["wind"]["speed"], "m/s")
        st.write("Humidity:", weather_data["main"]["humidity"], "%")
        st.write("\n")

        city_exists = True

    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException) as errh:
        st.write("Please enter a valid city name.")

def get_news(api_key, city_name):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        'q': city_name,
        'apiKey': api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        news_data = response.json()

        articles = news_data.get('articles', [])
        st.write('------------------------------------------')
        st.write("Top Headlines:")
        for index, article in enumerate(articles, start=1):
            st.write('------------------------------------------')
            st.write('\n' + f"Article {index}")
            st.write('\n' + f"Author: {article.get('author', 'N/A')}")
            st.write('\n' + f"Title: {article.get('title', 'N/A')}")
            st.write('\n' + f"Description: {article.get('description', 'N/A')}")
            st.write('\n' + f"Published on: {article.get('publishedAt', 'N/A')}")
            st.write('\n' + f"Content: {article.get('content', 'N/A')}")
            st.write('\n' + f"URL: {article.get('url', 'N/A')}")
        st.write('------------------------------------------')

    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException) as errh:
        st.write("Please enter a valid city name.")

def get_teleport_data(city_name):
    try:
        ua_endpoint = get_urban_area_endpoint(city_name)
        if ua_endpoint:
            details = get_area_details(ua_endpoint)
            images = get_area_images(ua_endpoint)
            scores = get_area_scores(ua_endpoint)
            
            st.write(f"\nUrban Area Development in {city_name}:")
            
            if details != 'not_found':
                st.write("\n**Area Details:**")
                for category, data in details.items():
                    st.write(f"\n*{category.capitalize()}*:")
                    for name, score in data.items():
                        st.write(f"{name}: {score}")
                
            if images != 'not_found':
                st.write("\n**Area Images:**")
                for img in images:
                    st.image(img['image']['web'])

            if scores != 'not_found':
                st.write("\n**Area Scores:**")
                for category, score in scores.items():
                    st.write(f"{category.capitalize()}: {score}")

    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException) as errh:
        st.write("Please enter a valid city name.")

def get_urban_area_endpoint(city_name):
    try:
        cities_endpoint = 'https://api.teleport.org/api/cities/'
        url = f'{cities_endpoint}?search={city_name}'
        
        r = requests.get(url)
        r.raise_for_status()
        r = r.json()
        geoname_url = r['_embedded']['city:search-results'][0]['_links']['city:item']['href']
        
        r2 = requests.get(geoname_url)
        r2.raise_for_status()
        r2 = r2.json()
        ua_endpoint = r2['_links']['city:urban_area']['href']
        return ua_endpoint

    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException) as errh:
        st.write("Please enter a valid city name.")
        return None

def get_area_details(ua_endpoint):
    try:
        r = requests.get(f"{ua_endpoint}details/")
        r.raise_for_status()
        r = r.json()

        result = {}

        for cat in r['categories']:
            result[cat['label']] = {}
            for i in cat['data']:
                name = i['label']
                key = next(k for k in i.keys() if 'value' in k)
                score = i[key]
                result[cat['label']][name] = score
        return result

    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException) as errh:
        st.write("Please enter a valid city name.")
        return 'not_found'

def get_area_images(ua_endpoint):
    try:
        r = requests.get(f"{ua_endpoint}images/")
        r.raise_for_status()
        r = r.json()
        return r['photos']

    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException) as errh:
        st.write("Please enter a valid city name.")
        return 'not_found'

def get_area_scores(ua_endpoint):
    try:
        r = requests.get(f"{ua_endpoint}scores/")
        r.raise_for_status()
        r = r.json()
        result = {i['name']: i['score_out_of_10'] for i in r['categories']}
        return result

    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException) as errh:
        st.write("Please enter a valid city name.")
        return 'not_found'

def main():
    # Replace with your API keys
    api_key_weather = "1c4aaa597dd29ba9c44da6839c89fbf6"
    api_key_news = "a3219de17f424b1380562001868597fe"

    if not api_key_weather or not api_key_news:
        st.write("Please provide API keys.")
        return

    styl = f"""
    <style>
        .made-by {{
          position: fixed;
          bottom: 10px;
          left: 600px;
          color: white;
        }}
        .source-code {{
          position: fixed;
          bottom: 10px;
          right: 700px;
          color: white;
        }}
    </style>
    """

    st.title("CityInsight 🌆🏢")

    city_name = st.text_input("Enter city name:")
    temperature_unit = st.text_input("Enter temperature unit (default is Celsius, enter 'imperial' for Fahrenheit): ")

    if temperature_unit.lower() not in ['metric', 'imperial']:
        temperature_unit = 'metric'

    if st.button("Get Weather, News, and Teleport Data"):
        get_weather(api_key_weather, city_name, temperature_unit)
        get_news(api_key_news, city_name)
        get_teleport_data(city_name)

    st.markdown("<div style='position: fixed; bottom: 10px; left: 600px; color: white;'>Made by <a href='https://github.com/Vikranth3140/' style='color:white; text-decoration:none;'>Vikranth Udandarao</a></div>", unsafe_allow_html=True)
    st.markdown("<div style='position: fixed; bottom: 10px; right: 700px; color: white;'><a href='https://github.com/Vikranth3140/CityInsight/' style='color:white; text-decoration:none;'>Source Code</a></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()