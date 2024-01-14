# import requests
# import streamlit as st
# import base64

# st.set_page_config(page_title="CityInsight", page_icon="🌆", layout="wide", initial_sidebar_state="expanded")

# city_exists = False

# def sidebar_bg(side_bg):
#     side_bg_ext = 'png'

#     st.markdown(
#         f"""
#         <style>
#         [data-testid="stSidebar"] > div:first-child {{
#             # background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open('{side_bg}', "rb").read()).decode()});
#             # background-size: cover;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

# def get_weather(api_key, city_name, temperature_unit='metric'):
#     global city_exists
#     base_url = "http://api.openweathermap.org/data/2.5/weather?"
#     complete_url = f"{base_url}appid={api_key}&q={city_name}&units={temperature_unit}"

#     if temperature_unit == 'metric':
#         temperature_unit = '°C'
#     else:
#         temperature_unit = '°F'

#     try:
#         response = requests.get(complete_url)
#         response.raise_for_status()
#         weather_data = response.json()

#         st.write("The weather in " + city_name + " is:")
#         st.write("Weather:", weather_data["weather"][0]["description"])
#         st.write("Temperature:", weather_data["main"]["temp"], f"{temperature_unit.upper()}")
#         st.write("Wind Speed:", weather_data["wind"]["speed"], "m/s")
#         st.write("Humidity:", weather_data["main"]["humidity"], "%")
#         st.write("\n")

#         city_exists = True

#     except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException) as errh:
#         st.write("Please enter a valid city name.")

# def get_news(api_key, city_name):
#     url = f'https://newsapi.org/v2/top-headlines?q={city_name}&' f'apiKey={api_key}'

#     if not city_exists:
#         return

#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         news_data = response.json()

#         articles = news_data['articles']
#         st.write('------------------------------------------')
#         st.write("Top Headlines:")
#         for index, article in enumerate(articles, start=1):
#             st.write('------------------------------------------')
#             st.write('\n' + f"Article {index}")
#             st.write('\n' + f"Author")
#             st.write(article['author'])
#             st.write('\n' + f"Title")
#             st.write(article['title'])
#             st.write('\n' + f"Description")
#             st.write(article['description'])
#             st.write('\n' + f"Published on")
#             st.write(article['publishedAt'])
#             st.write('\n' + f"Content")
#             st.write(article['content'])
#             st.write('\n' + f"URL")
#             st.write(article['url'])

#     except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException) as errh:
#         st.write("Please enter a valid city name.")

# def get_teleport_data(city_name):
#     ua_endpoint = get_urban_area_endpoint(city_name)
#     results = {}
#     if ua_endpoint:
#         details = get_area_details(ua_endpoint)
#         results['details'] = details
#         images = get_area_images(ua_endpoint)
#         results['images'] = images
#         scores = get_area_scores(ua_endpoint)
#         results['scores'] = scores
#     return results


# def get_urban_area_endpoint(city_name):
#     try:
#         cities_endpoint = 'https://api.teleport.org/api/cities/'
#         url = f'{cities_endpoint}?search={city_name}'
        
#         r = requests.get(url)
#         r = r.json()
#         r['_embedded']
#         geoname_url = r['_embedded']['city:search-results'][0]['_links']['city:item']['href']
        
#         r2 = requests.get(geoname_url)
#         r2 = r2.json()
#         ua_endpoint = r2['_links']['city:urban_area']['href']
#         return ua_endpoint
#     except:
#         return None

# def get_area_details(ua_endpoint):
#     try:
#         r = requests.get(ua_endpoint + 'details/')
#         r = r.json()

#         result = {}

#         for cat in r['categories']:
#             result[cat['label']] = {}
#             for i in cat['data']:
#                 name = i['label']
#                 key = [k for k in i.keys() if 'value' in k][0]
#                 score = i[key]
#                 # result[name] = score
#                 result[cat['label']][name] = score
#         return result
#     except:
#         return 'not_found'


# def get_area_images(ua_endpoint):
#     try:
#         r = requests.get(ua_endpoint + 'images/')
#         r = r.json()
#         return r['photos']
#     except:
#         return 'not_found'


# def get_area_scores(ua_endpoint):
#     try:
#         r = requests.get(ua_endpoint + 'scores/')
#         r = r.json()
#         result = {}
#         for i in r['categories']:
#             name = i['name']
#             score = i['score_out_of_10']
#             result[name] = score
#         return result
#     except:
#         return 'not_found'

# def main():
#     # Replace with your API keys
#     api_key_weather = "1c4aaa597dd29ba9c44da6839c89fbf6"
#     api_key_news = "a3219de17f424b1380562001868597fe"

#     if not api_key_weather or not api_key_news:
#         st.write("Please provide API keys.")
#         return

#     # side_bg = "assets\city.png"
#     # sidebar_bg(side_bg)

#     styl = f"""
#     <style>
#         .made-by {{
#           position: fixed;
#           bottom: 10px;
#           left: 600px;
#           color: white;
#         }}
#         .source-code {{
#           position: fixed;
#           bottom: 10px;
#           right: 700px;
#           color: white;
#         }}
#     </style>
#     """

#     st.markdown(styl, unsafe_allow_html=True)

#     st.title("CityInsight🌆🏢")

#     city_name = st.text_input("Enter city name:")
#     temperature_unit = st.text_input("Enter temperature unit (default is Celsius, enter 'imperial' for Fahrenheit): ")

#     if temperature_unit.lower() not in ['metric', 'imperial']:
#         temperature_unit = 'metric'

#     if st.button("Get Weather and News"):
#         get_weather(api_key_weather, city_name, temperature_unit)
#         get_news(api_key_news, city_name)

#     st.markdown("<div class='made-by'>Made by <a href='https://github.com/Vikranth3140/' style='color:white; text-decoration:none;'>Vikranth Udandarao</a></div>", unsafe_allow_html=True)
#     st.markdown("<div class='source-code'><a href='https://github.com/Vikranth3140/CityInsight/' style='color:white; text-decoration:none;'>Source Code</a></div>", unsafe_allow_html=True)

#     results = get_teleport_data(city_name)
#     results['images']
#     results['scores']

# if __name__ == "__main__":
#     main()


















































































import requests
import streamlit as st

def get_weather(api_key, city_name, temperature_unit='metric'):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': temperature_unit
    }

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

    except requests.exceptions.RequestException as err:
        st.write("Error fetching weather data:", err)

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

    except requests.exceptions.RequestException as err:
        st.write("Error fetching news data:", err)

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

    except requests.exceptions.RequestException as err:
        st.write("Error fetching Teleport data:", err)

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

    except requests.exceptions.RequestException as err:
        st.write("Error fetching Urban Area Endpoint:", err)
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

    except requests.exceptions.RequestException as err:
        st.write("Error fetching Area Details:", err)
        return 'not_found'

def get_area_images(ua_endpoint):
    try:
        r = requests.get(f"{ua_endpoint}images/")
        r.raise_for_status()
        r = r.json()
        return r['photos']

    except requests.exceptions.RequestException as err:
        st.write("Error fetching Area Images:", err)
        return 'not_found'

def get_area_scores(ua_endpoint):
    try:
        r = requests.get(f"{ua_endpoint}scores/")
        r.raise_for_status()
        r = r.json()
        result = {i['name']: i['score_out_of_10'] for i in r['categories']}
        return result

    except requests.exceptions.RequestException as err:
        st.write("Error fetching Area Scores:", err)
        return 'not_found'

def main():
    # Replace with your API keys
    api_key_weather = "1c4aaa597dd29ba9c44da6839c89fbf6"
    api_key_news = "a3219de17f424b1380562001868597fe"

    if not api_key_weather or not api_key_news:
        st.write("Please provide API keys.")
        return

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
    st.markdown("<div style='position: fixed; bottom: 10px; right: 700px; color: white;'>Source Code <a href='https://github.com/Vikranth3140/CityInsight/' style='color:white; text-decoration:none;'>GitHub</a></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()