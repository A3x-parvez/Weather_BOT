import requests
import telebot 
import datetime
import sys
from keys import BOT_Token,Visual_API


API=Visual_API
TELEGRAM_BOT_TOKEN = BOT_Token
bot = telebot.TeleBot(BOT_Token)

#Current time 
def get_current_hour():
    # Get the current time
    current_time = datetime.datetime.now()
    # Extract the current hour (0-23)
    current_hour = current_time.hour
    return current_hour

#weather report getting function.
def get_weather_report(area,hour):
    response = requests.request("GET", f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{area}?unitGroup=metric&include=current%2Cdays%2Chours&key={API}&contentType=json")
    if response.status_code!=200:
        print('Unexpected Status code: ', response.status_code)
        report =(
            f"Area not found or something went wrong.please try again."
        )
        sys.exit()
        
    #get data into jsonfile
    jsonData = response.json()
    weather_data = jsonData
    # Extract relevant data
    current_conditions = weather_data['currentConditions']
    current_date = weather_data['days'][0]['datetime']
    latest_hour = weather_data['days'][0]['hours'][hour]  # Latest hour's update
    resolved_address = weather_data['resolvedAddress']
    address = weather_data['address']
    windspeed = latest_hour['windspeed']
    temp = current_conditions['temp']
    feelslike = current_conditions['feelslike']
    condition = current_conditions['conditions']
    description = weather_data['days'][0]['description']
    humidity = latest_hour['humidity']
    air_pressure = latest_hour['pressure']
    sunrise = weather_data['currentConditions']['sunrise']
    sunset = weather_data['currentConditions']['sunset']

    #feedback message
    # Create a personalized message based on the weather condition
    if "rain" in description:
        personal_msg = "🌧️ It looks like rain today! Don't forget your umbrella, and stay cozy! ☔"
    elif "clear" in description or "sunny" in description:
        personal_msg = "☀️ The sun is shining bright! Grab your sunglasses and enjoy the beautiful day! 😎"
    elif "snow" in description:
        personal_msg = "❄️ It's going to snow! Bundle up and stay warm! 🧣🧤"
    elif "storm" in description:
        personal_msg = "⛈️ A storm might be coming, so please stay safe and don't forget your umbrella! 🌂"
    elif "cloudy" in description:
        personal_msg = "☁️ It's a cloudy day ahead. You might want to keep an umbrella handy, just in case! 🌂"
    else:
        personal_msg = "🌈 Wishing you a wonderful day, no matter the weather! 😊"
        
        
    # Format the weather report
    report = (
        f"🌍 Weather Report for {resolved_address}.\n\n"
        f"🌆 Area : {address}\n"
        f"📅 Date : {current_date}\n"
        f"🕒 Last update time : {latest_hour['datetime']}\n"
        f"🌥️ Today's sky : {condition}\n"
        f"🌤️ Weather : {description}\n"
        f"🌡️ Temperature : {temp}°C\n"
        f"🌡️ Temperature feels like: {feelslike}°C\n"
        f"🌪️ Windspeed : {windspeed} km/h\n"
        f"💧 Humidity : {humidity}%\n"
        f"🛬 Air Pressure : {air_pressure} hPa\n"
        f"🌄 Sunrise : {sunrise}\n"
        f"🌆 Sunset : {sunset}\n\n"
        f"😀 Advice : {personal_msg}"
    )
    
    return report

# Function to handle the /start command
@bot.message_handler(['start'])
def start(message):
     bot.reply_to(message,f"Hello there! 😊 I'm your friendly Weather_BOT! 🌦️ Just send me the name of your city, and I'll happily share the latest weather update with you! 🌤️✨")
     print("user start the services.")
    
# Function to handle incoming messages (city names)
@bot.message_handler()
def handle_message(message):
        print("Fetch current time.")
        hour = get_current_hour()
        print("Access latest update.")
        #recived area name.
        city = message.text
        print("Area name recived.")
        weather_report =get_weather_report(area=city,hour=hour)
        print("Weather information fetched.")
        bot.reply_to(message,weather_report)
        print("Responce send sucessfully.")

def main():
    print("Bot starting....")
    bot.polling()

#main program start from here
if __name__ == '__main__':
    main()
