import telebot
import requests
from telebot import types

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"



bot = telebot.TeleBot(TOKEN)
chat_ids = set()

# Словник з даними про місця в різних містах України
places_data = {
    "Київ": {
        "Готелі 🏨": ["Hilton Kyiv", "Premier Hotel Rus", "Fairmont Grand Hotel Kyiv"],
        "Ресторани 🍽️": ["Ресторан Матісс", "Very Well Cafe", "Art Eclair"],
        "Магазини 🏪🛒": ["АТБ-Маркет", "Fozzy", "ЭКО маркет"],
        "Цікаві місця Києва 🏞️": ["Галерея «Парсуна»", "Феофанія", "Київський водоспад"]
    },
    "Одеса": {
        "Готелі 🏨": ["Bristol Hotel", "Hotel Milano", "Отель Дюк"],
        "Ресторани 🍽️": ["Dacha", "Moondeer", "Foundation Coffee Roasters"],
        "Магазини 🏪🛒": ["Таврія В", "Сільпо", "АТБ-Маркет"],
        "Цікаві місця Одеси 🏞️": ["Дерибасівська", "Потьомкінські сходи", "Одеський оперний театр"]
    },
    "Харків": {
        "Готелі 🏨": ["Kharkiv Palace Hotel", "Superior Golf & Spa Resort", "Hotel 19"],
        "Ресторани 🍽️": ["Park Місто", "Sandy Bar", "Цукат"],
        "Магазини 🏪🛒": ["Karavan", "Ашан", "Метро"],
        "Цікаві місця Харкова 🏞️": ["Городская Ратуша", "Городской Парк Горького", "Музей історії Харкова"]
    },
    "Вінниця": {
        "Готелі 🏨": ["Optima Vinnytsia Hotel", "Fenix Hotel", "Hotel France"],
        "Ресторани 🍽️": ["Кафе Бібліотека", "Ресторан Аристократ", "Ресторан Clover"],
        "Магазини 🏪🛒": ["Мегамаркет", "АТБ-Маркет", "Сільпо"],
        "Цікаві місця Вінниці 🏞️": ["Навчальний фермерський музей", "Собор Святої Марії", "Парк Горького"]
    },
    "Львів": {
        "Готелі 🏨": ["Leopolis Hotel", "Nobilis Hotel", "Bank Hotel"],
        "Ресторани 🍽️": ["Kryivka", "Цукор RED", "Teddy Restaurant"],
        "Магазини 🏪🛒": ["Forum Lviv", "Рукавичка", "Сільпо"],
        "Цікаві місця Львова 🏞️": ["Ратуша", "Площа Ринок", "Львівська Опера"]
    },
    "Ужгород": {
        "Готелі 🏨": ["Hotel Kilikiya ", "Ungvarskiy Hotel ", "Hotel Europe "],
        "Ресторани 🍽️": ["Кілікія ", "Ресторан «Татош»", "Деца у Нотаря "],
        "Магазини 🏪🛒": ["Сільпо ", "Tokyo – торгово-розважальний комплекс ", "АТБ-Маркет"],
        "Цікаві місця Ужгорода 🏞️": ["Закарпатський музей унікальності та рідкісності ", "Ужгородський замок ",
                                      "Площа Корятовича "]
    }
}

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"].capitalize()
        temperature = data["main"]["temp"]
        return f"Погода в {city}:\n{weather_description}, Температура 🌡️: {temperature}°C"
    else:
        return "Не вдалося отримати дані про погоду для цього міста."

def create_about_button():
    about_button = types.KeyboardButton("Помічник Мандрівників ℹ️")
    return about_button

def create_city_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_kiev = types.KeyboardButton("Київ ⭐️")
    button_odessa = types.KeyboardButton("Одеса ☀️ 🌊")
    button_kharkiv = types.KeyboardButton("Харків 🏞️")
    button_vinnitsa = types.KeyboardButton("Вінниця 🍇")
    button_lviv = types.KeyboardButton("Львів 🏙️")
    button_uzhgorod = types.KeyboardButton("Ужгород 🌃")
    button_about = create_about_button()
    markup.add(button_kiev, button_odessa, button_kharkiv, button_vinnitsa, button_lviv, button_uzhgorod, button_about)
    return markup

def send_help(message):
    help_text = "Для початку виберіть місто, а потім отримайте інформацію про готелі, ресторани, магазини та цікаві місця цього міста. Щоб дізнатися про погоду, просто напишіть назву міста."
    bot.send_message(message.chat.id, help_text)

# Обробник команди /help
@bot.message_handler(commands=['help'])
def send_help_message(message):
    send_help(message)

# Обробник повідомлень користувачів з ключовим словом "help"
@bot.message_handler(func=lambda message: "help" in message.text.lower())
def send_help_on_request(message):
    send_help(message)

# Обробник команди /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Бот знову активний! Виберіть місто:", reply_markup=create_city_keyboard())
    commands_list = "Список доступних команд:\n/start - вибрати місто\n/help - отримати довідку"
    bot.send_message(message.chat.id, commands_list)

# Обробник повідомлень користувачів
@bot.message_handler(func=lambda message: True)
def send_places(message):
    if message.text == "Помічник Мандрівників ℹ️":
        about_text = "Ваш вірний супутник для подорожей по Україні! Знайдіть найцікавіші маршрути, дізнайтеся про історію та культуру різних регіонів і створіть неперевершені спогади разом із нашим помічником."
        bot.send_message(message.chat.id, about_text)
    else:
        city = message.text.split()[0]
        if city in places_data:
            reply = f"Ось що я знайшов для міста {city}:\n"
            for category, places in places_data[city].items():
                reply += f"\n{category}:\n"
                reply += "\n".join(places)
                reply += "\n"
            bot.send_message(message.chat.id, reply)
            if city == "Київ":
                bot.send_location(message.chat.id, latitude=50.4501, longitude=30.5234)
            elif city == "Одеса":
                bot.send_location(message.chat.id, latitude=46.4825, longitude=30.7233)
            elif city == "Харків":
                bot.send_location(message.chat.id, latitude=49.9935, longitude=36.2304)
            elif city == "Вінниця":
                bot.send_location(message.chat.id, latitude=49.2331, longitude=28.4682)
            elif city == "Львів":
                bot.send_location(message.chat.id, latitude=49.8397, longitude=24.0297)
            elif city == "Ужгород":
                bot.send_location(message.chat.id, latitude=48.6208, longitude=22.2879)
            weather_info = get_weather(city)
            bot.send_message(message.chat.id, weather_info)
        else:
            bot.send_message(message.chat.id, "На жаль, я не знаю такого міста. Спробуйте інше.")

def on_polling_start():
    for chat_id in chat_ids:
        bot.send_message(chat_id, "Бот знову активний! Виберіть місто:", reply_markup=create_city_keyboard())

if __name__ == '__main__':
    on_polling_start()
    bot.polling()
