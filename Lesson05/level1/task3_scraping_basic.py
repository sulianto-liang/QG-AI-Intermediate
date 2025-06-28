# File: task3_scraping_basic.py
from bs4 import BeautifulSoup
import csv

def scrape_weather_data(html_content):
    """Extract city, temperature, condition from sample HTML"""
    # TODO: Parse HTML and extract weather data for 5 Indonesian cities
    # TODO: Save to CSV with headers: city, temperature, condition, humidity

    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract title
    title = soup.find('title').text
    print(f"✅ Page title: {title}")

    # Extract all weather items
    weather_items = soup.find_all('section', class_='weather-item')
    print(f"✅ Found {len(weather_items)} weather items:")

    for i, item in enumerate(weather_items, 1):
        city = item.find('h2').text
        temperature = item.find('p', class_='temperature').text
        condition = item.find('div', class_='condition').text
        humidity = item.find('span', class_='humidity').text
        date = item.find('span', class_='date').text
        time = item.find('p', class_='time').text

        print(f"   {i}. {city}")
        print(f"      Temperature: {temperature}")
        print(f"      Condition: {condition}")
        print(f"      Humidity: {humidity}")
        print(f"      Date: {date}")
        print(f"      Time: {time}")

# Sample HTML provided with Jakarta, Surabaya, Bandung, Medan, Yogyakarta data
sample_html = """
    <html>
        <head><title>Indonesian Weather Report</title></head>
        <body>
            <h1>Indonesian Weather Report</h1>
            <div class="weather-container">
                <section class="weather-item">
                    <h2>Jakarta</h2>
                    <p class="time">16.30 WIB</p>
                    <span class="date">2025-06-28</span>
                    <p class="temperature">27 °C</p>
                    <div class="condition">Cloudy</div>
                    <span class="humidity">70%</span>
                </section>
                <section class="weather-item">
                    <h2>Surabaya</h2>
                    <p class="time">16.40 WIB</p>
                    <span class="date">2025-06-28</span>
                    <p class="temperature">30 °C</p>
                    <div class="condition">Sunny</div>
                    <span class="humidity">60%</span>
                </section>
                <section class="weather-item">
                    <h2>Bandung</h2>
                    <p class="time">16.35 WIB</p>
                    <span class="date">2025-06-28</span>
                    <p class="temperature">22 °C</p>
                    <div class="condition">Rainy</div>
                    <span class="humidity">80%</span>
                </section>
                <section class="weather-item">
                    <h2>Medan</h2>
                    <p class="time">16.25 WIB</p>
                    <span class="date">2025-06-28</span>
                    <p class="temperature">33 °C</p>
                    <div class="condition">Sunny</div>
                    <span class="humidity">75%</span>
                </section>
                <section class="weather-item">
                    <h2>Yogyakarta</h2>
                    <p class="time">16.30 WIB</p>
                    <span class="date">2025-06-28</span>
                    <p class="temperature">24 °C</p>
                    <div class="condition">Rainy</div>
                    <span class="humidity">85%</span>
                </section>
            </div>
        </body>
    </html>
    """

scrape_weather_data(sample_html)
