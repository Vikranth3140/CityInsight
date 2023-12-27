# CityInsight 🌆📰🌦️

CityInsight is a Python application that integrates weather and news information, providing city-centric insights. Built with Streamlit, it offers real-time weather updates and top headlines tailored to your chosen city.

Currently deployed at <a href="https://cityinsight.streamlit.app/">CityInsight<a>

## Overview

CityInsight combines OpenWeatherMap and NewsAPI to deliver a comprehensive view of your city's current conditions and the latest news.

## Features

1. **Weather Insights:**
   - Real-time weather data retrieval using OpenWeatherMap API.
   - Displays current weather conditions, temperature, wind speed, and humidity.

2. **News Highlights:**
   - Fetches top headlines from NewsAPI.
   - Provides details such as title, description, publication date, and content for each news article.

## How to Use

1. **Installation:**
   - Clone the repository.

    ```bash
    git clone https://github.com/Vikranth3140/CityInsight.git
    ```

   - Install required dependencies

    ```bash
    pip install -r requirements.txt
    ```

2. **API Configuration:**
   - Obtain API keys from [OpenWeatherMap](https://openweathermap.org/api) and [NewsAPI](https://newsapi.org/).
   - Replace placeholders in the script (`api_key_weather` and `api_key_news`) with your actual keys.

3. **Run the Application:**
   - Execute the Streamlit app

    ```bash
    streamlit run cityinsight.py
    ```

   - Enter the desired city name and choose the temperature unit ('metric' or 'imperial').

4. **View Insights:**
   - The application will display real-time weather information and top news headlines tailored to your selected city.

## Requirements

- Python 3.x
- Streamlit
- Requests library

## Note

- Keep your API keys confidential and do not share them publicly.
- Ensure an active internet connection for accurate data retrieval.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

[Vikranth Udandarao](https://github.com/Vikranth3140)
