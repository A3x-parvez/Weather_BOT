import requests
import telebot
from keys import *

TELEGRAM_BOT_TOKEN = BOT_Token
WEATHER_API_KEY = API_Key

bot = telebot.TeleBot(BOT_Token)

    
# Function to get weather data for a given city
def get_weather(city):
    WEATHER_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(WEATHER_URL)
    data = response.json()

    if data['cod'] == 200:  # Check for successful response
        weather_desc = data['weather'][0]['description'].lower()
        sky = data['weather'][0]['main']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        #avg_temp = (float(data['temp_min'])+float(data['temp_max']))/2
        air_press = data['main']['pressure']
        wind_speed = data['wind']['speed']
        humidity = data['main']['humidity']
        
        # Create a personalized message based on the weather condition
        if "rain" in weather_desc:
            personal_msg = "It might rain , don't forget to carry an umbrella!"
        elif "clear" in weather_desc or "sunny" in weather_desc:
            personal_msg = "It's sunny, wear sunglasses!"
        elif "snow" in weather_desc:
            personal_msg = "Snowfall expected, dress warmly!"
        elif "storm" in weather_desc:
            personal_msg = "Stormy weather, stay safe!"
        else:
            personal_msg = "Enjoy your day!"

        weather_report = (
            f"Weather in {city.capitalize()}: {weather_desc.capitalize()}\n"
            f"Temperature: {temp}°C\n"
            f"Feels like: {feels_like}°C\n"
            # f"Avg temperature: {avg_temp}°C\n"
            f"Humidity: {humidity}%\n"
            f"Sky: {sky}\n"
            f"Air pressure: {air_press}hPa\n"
            f"Wind speed: {wind_speed}mph\n"
            f"{personal_msg}"
        )
        return weather_report
        # return data
    else:
        return "Sorry, I couldn't retrieve the weather for that city."



# Function to handle the /start command
@bot.message_handler(['start'])
def start(message):
     bot.reply_to(message,"Welcome! Send me a city name, and I'll give you the current weather forecast!")
 # Function to handle incoming messages (city names)
@bot.message_handler()
def handle_message(message):
     city = message.text
     weather_report = get_weather(city)
     bot.reply_to(message,weather_report)


def main():
    print("Bot starting....")
    bot.polling()

if __name__ == '__main__':
    main()
