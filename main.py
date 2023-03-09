import asyncio

import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = "https://meteum.ai/?lat=28.49462128&lon=-11.32948112"


async def fetch_weather():
    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the weather data
    temperature = soup.find('span', {'class': 'temp__value temp__value_with-unit'}).text
    condition = soup.find('div', {'class': 'link__condition day-anchor i-bem'}).text

    # Return the weather data
    return f"The temperature is {temperature} and the condition is {condition}"


async def main():
    # Wait for the response from the server
    weather_data = await fetch_weather()

    # Print the weather data
    print(weather_data)


# Run the asyncio event loop
asyncio.run(main())
