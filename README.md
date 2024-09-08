# Weather_BOT🌦️

This is a Python-based Telegram bot that provides real-time weather updates for any city. The bot retrieves weather information using the Visual Crossing API and sends a detailed report to users on Telegram. The weather report includes information like temperature, humidity, wind speed, air pressure, and more.

## Features ✨
- Provides weather reports for any city in the world.
- Extracts weather data including temperature, feels-like temperature, humidity, wind speed, and air pressure.
- Offers personalized messages based on the current weather conditions (e.g., rain, sunny, snow, etc.).
- Sends sunrise and sunset times.
- Automatically fetches and updates weather data for the latest hour.

## Prerequisites 📋

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your local machine.
- A Telegram bot token. You can obtain this by creating a bot using the [BotFather](https://core.telegram.org/bots#botfather).
- An API key or URL link from [Visual Crossing](https://www.visualcrossing.com/) for weather data retrieval.
- Install the required Python packages:
  ```bash
  pip install requests telebot
  ```
## Installation and Setup ⚙️

#### Clone the repository:

```bash
git clone https://github.com/A3x-parvez/Weather_BOT.git
```
#### Install the required dependencies:
```bash
pip install telebot
```
```bash
pip install requests
```
#### Obtain your Telegram bot token by creating a bot using BotFather on Telegram. Add the token in a file named `main_v2.py` as follows:
```bash
BOT_Token = "YOUR_TELEGRAM_BOT_TOKEN"
```
#### Obtain an API key from Visual Crossing and replace it in the `get_weather_report()` function of the `main_v2.py` file.

#### Run the bot:
```bash
python main_v2.py
```
## Usage 🚀
Start a conversation with your bot on Telegram.
Type `/start` to initiate the bot.
Send your city name to get a real-time weather report.
```bash
User : /start
Bot :
Hello there! 😊 I'm your friendly Weather_BOT! 🌦️ Just send me the name of your city, and I'll happily share the latest weather update with you! 🌤️✨
User : Bolpur 
Bot :
🌍 Weather Report for Bolpur, Bolpur Sriniketan, West Bengal, India.

🌆 Area : Bolpur
📅 Date : 2024-09-08
🕒 Last update time : 15:00:00
🌥️ Today's sky : Rain, Overcast
🌤️ Weather : Becoming cloudy in the afternoon with storms possible.
🌡️ Temperature : 34.9°C
🌡️ Temperature feels like: 41.4°C
🌪️ Windspeed : 13.3 km/h
💧 Humidity : 52.66%
🛬 Air Pressure : 999.0 hPa
🌄 Sunrise : 05:23:23
🌆 Sunset : 17:50:00

😀 Advice : ⛈️ A storm might be coming, so please stay safe and don't forget your umbrella! 🌂
```

## Contribution 🤝

Contributions are always welcome! Feel free to submit a pull request or report issues.

## Contact me 📞
If you have any questions or feedback, feel free to reach out:

 - GitHub: A3x-parvez 
 - LinkedIn: Rijwanool Karim 
 - Email: rijwanoolkarim143r@gmail.com

## Thank you for visiting my profile.❤️😊 
