import telebot
import requests
import json

API_TOKEN = '6861440713:AAF4i5u1u-YxAS1plhDTsMYNKcTLA-aT3Cc'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")
    
city = ""
    
@bot.message_handler(commands=['weather'])
def get_weather(message):
    global city 
    # get city name 
    city = "Dushanbe"

    # city lati long

    city_lati = "38.5598"
    city_long = "68.7870"
    
    # get information

    address = f"https://api.open-meteo.com/v1/forecast?latitude={city_lati}&longitude={city_long}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    data = requests.get(address)
    data = json.loads(data.text)

    result = ""
    
    for key, value in data.items():
        if key == "current":
            for k, v in value.items():
                if k == "temperature_2m":
                    result = v

    # show to user
    bot.reply_to(message, f"{city}: {result} °C")



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    
    bot.reply_to(message, message.text)


bot.infinity_polling()