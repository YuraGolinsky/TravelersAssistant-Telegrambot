Ссылки на телеграмм бот: https://t.me/TravelinUkraineAssistant_Bot

Инструкция
Начало работы бота: Когда вы впервые взаимодействуете с ботом, он приветствует вас и предлагает выбрать город для поездки. Это можно сделать, нажав на кнопки с названиями городов или кнопку "Помощник Путешественников ℹ️" для получения дополнительной информации о боте.
Выбор города: После выбора города вы получите информацию об отелях, ресторанах, магазинах и интересных местах этого города. Бот также отправит вам географические координаты этого места и информацию о погоде в этом городе.
 Помощь: Если у вас есть вопросы или вы нуждаетесь в помощи, вы можете воспользоваться командой /help или просто написать слово "help" в вашем сообщении. Бот пришлет вам инструкции по использованию его функций.
Дополнительные команды: Кроме команды /help, вы можете воспользоваться командой /start, чтобы выбрать город снова. Бот также будет посылать вам сообщения о том, что он снова активен, вместе с кнопками для выбора города, когда вы впервые начинаете общение с ним.

Создание бот имеет несколько функций, позволяющих пользователям получать информацию о разных местах в разных городах Украины, а также узнавать погоду в этих городах.

Выбор города: Пользователь может выбрать один из городов Украины, для которого хочет получить информацию о разных местах.
Получение информации о местах После выбора города пользователь получает информацию о разных категориях мест в таких городах, как гостиницы, рестораны, магазины и интересные места.
 Отображение мест на карте: Помимо информации о местах, пользователь может просмотреть расположение этих мест на карте, чтобы легче сориентироваться в городе.
 Кроме того, пользователь может узнать погоду в выбранном городе. Бот использует погодные API для получения текущих погодных данных, таких как погода и температура.
Дополнительная информация: Кроме того, пользователь может получить дополнительную информацию о работе, например, описание его функций или возможностей.

Бот является полезным помощником для путешественников, который дает информацию о местах (гостиницах, ресторанах, магазинах, интересных местах города) и погоде в разных городах Украины, а также помогает сориентироваться на карте.

Создание ботов на Python стало популярным по нескольким причинам:
Python - это высокоуровневый язык программирования общего назначения, известный своей простотой, понятностью синтаксиса и широким спектром применений. Она широко используется для разработки веб-приложений, научных вычислений, искусственного интеллекта, анализа данных, разработки игр и многое другое.
Простота изучения и использования: Python имеет читальный синтаксис и простую структуру, что делает его идеальным для начинающих. Это позволяет быстро разрабатывать и настраивать ботов без усилий.
Широкие возможности: Python имеет множество библиотек и фреймворков, которые помогают разработчикам создавать различные функции для своих ботов. Это включает в себя библиотеки для работы с API социальных сетей, обработки естественного языка, создания веб-интерфейсов и многое другое.
 Поддержка Telegram Bot API: Telegram предоставляет API, позволяющее создавать ботов для этой платформы. Библиотеки Python, такие как telebot, обеспечивают простой способ взаимодействия с этим API и разработки функций для ботов.
Активное сообщество разработчиков: Python имеет большое и активное сообщество разработчиков, которое оказывает поддержку, ресурсы и советы. Это делает процесс разработки ботов на Python более доступным и приятным.
Кросс-платформенность: Python код может запускаться на различных операционных системах, что делает работы более гибкими и доступными для разных пользователей.

В коде используются следующие инструменты и библиотеки

1. Telebot (TeleBot):
     – Это библиотека для работы с Telegram Bot API в Python.
Телеграмм-бот (TeleBot) – это приложение, которое автоматизирует взаимодействие с пользователями через мессенджер Telegram с помощью API Telegram Bot. Такой бот может отправлять сообщения, взаимодействовать с командами пользователей, получать входящие сообщения, отвечать на них, реагировать на события и прочее.
     - Функциональность: Позволяет создавать, настраивать и управлять ботами в Telegram, включая обработку входящих сообщений, отправку сообщений пользователям и создание клавиатур для взаимодействия с ними.
     - Использование в коде: Библиотека импортируется с помощью `import telebot`, а сам бот создается с помощью `telebot.TeleBot(TOKEN)`.
API (Application Programming Interface) – это набор правил и протоколов, определяющих, как один программный компонент взаимодействует с другим. API определяет, какие функции и операции может использовать один программный компонент для общения с другими компонентами или сервисами
2. requests:
     - Это библиотека для выполнения HTTP-запросов в Python.
     - Функциональность: Позволяет получать данные из веб-серверов, используя различные методы запросов, такие как GET, POST, PUT и т.д.
     - Использование в коде: используется для получения данных о погоде с внешнего API с помощью HTTP-запросов.
3. типы с telebot:
     - Назначение: Это модуль для использование типов сообщений Telegram в библиотеке telebot.
    - Функциональность: Позволяет создавать различные типы сообщений, включая клавиатуры, стикеры, медиафайлы и т.д.
    - Использование в коде: используется для создания клавиатур для взаимодействия с пользователями и других объектов, таких как кнопки.
4. api.openweathermap.org:
    - Назначение: Это веб-API для получения информации о погоде.
    - Функциональность: Предоставляет доступ к актуальным данным о погоде в разных местах по всему миру.
    - Использование кода: Используется для получения информации о погоде в разных городах, чтобы бот мог сообщить пользователям о текущих погодных условиях.
WEATHER_API_KEY – это переменная, содержащая ключ доступа к погодному API, используемый для получения информации о погоде внешнего сервиса. Ключ API – это уникальный идентификатор, предоставляемый при регистрации в сервисе, предоставляемом API. Обычно это необходимо для аутентификации запросов к сервису и доступа к его функционалу.

5. set():
    - Назначение: Это структура данных в Python, которая представляет собой неупорядоченную коллекцию уникальных элементов.
    - Функциональность: Она используется для хранения уникальных чат-идентификаторов, чтобы бот мог отправлять сообщения многим пользователям одновременно.
    - Использование в коде: Используется для хранения чат-идентификаторов пользователей, которым нужно отправить сообщение.
6. Places_data - это словарь в используемом коде, содержащий данные о разных местах в разных городах Украины. Данный словарь содержит информацию об отелях, ресторанах, магазинах и интересных местах в таких городах, как Киев, Одесса, Харьков, Винница, Львов и Ужгород.

В коде используется карта для отображения местоположения в разных городах Украины. В коде используется функция bot.send_location(), позволяющая отправлять пользователям координаты места на карте.

Вот как работает эта функция:
Вы вызываете функцию bot.send_location() с параметрами chat_id, latitude и longitude.
chat_id – это уникальный идентификатор чата или пользователя, куда вы хотите отправить местоположение.
latitude и longitude – это координаты места, которое вы хотите показать на карте. Координата latitude указывает на северную или южную широту, а координата longitude – на восточную или западную долготу.
Пример: bot.send_location(chat_id, latitude=49.8397, longitude=24.0297)
В этом примере latitude=49.8397 и longitude=24.0297 отвечают за координаты места во Львове. После вызова этой функции пользователь получит сообщение с местоположением, которое отобразится на карте в чате с ботом.


Запуск бота // Launching a bot
![image](https://github.com/YuraGolinsky/TravelersAssistant/assets/134283897/766b9d86-d75d-4c35-a5ab-b8b48cb38962)

Кнопки для вибору міста бот // Buttons for choosing the bot city
![image](https://github.com/YuraGolinsky/TravelersAssistant/assets/134283897/d54f6f42-0030-4f20-afe4-516c55f34451)

Інформація про місто // Information about the city
![image](https://github.com/YuraGolinsky/TravelersAssistant/assets/134283897/d7b473c8-03b5-4e37-8649-9203318c20ac)


Інформація про Бот // Information about Bot
![image](https://github.com/YuraGolinsky/TravelersAssistant/assets/134283897/c115e8ed-afad-40eb-af83-21307e903843)
![image](https://github.com/YuraGolinsky/TravelersAssistant/assets/134283897/94661ee7-f0f2-439b-8d35-b8e3837f76a3)


Translation into English


Telegram bot link: https://t.me/TravelinUkraineAssistant_Bot

Instruction
Starting the bot: When you first interact with the bot, it greets you and prompts you to choose a city to travel to. This can be done by clicking on the buttons with the names of the cities or on the "Traveler's Assistant ℹ️" button for more information about the bot.
Selecting a city: After selecting a city, you will receive information about hotels, restaurants, shops and interesting places in that city. The bot will also send you the geographic coordinates of that location and information about the weather in that city.
Help: If you have a question or need help, you can use the /help command or simply write the word "help" in your message. The bot will send you instructions on how to use its features.
Additional commands: In addition to the /help command, you can use the /start command to select the city again. The bot will also send you a message that it's active again, along with buttons to select a city, when you first start chatting with it.

The created bot has several functions that allow users to get information about different places in different cities of Ukraine, as well as find out the weather in these cities.

Choosing a city: The user can choose one of the cities of Ukraine for which he wants to receive information about various places.
Retrieving information about places After selecting a city, the user receives information about different categories of places in the city, such as hotels, restaurants, shops and points of interest.
Displaying places on the map: In addition to information about places, the user can view the location of these places on the map to find their way around the city more easily.
In addition, the user can find out the weather in the selected city. The bot uses weather APIs to get up-to-date weather data such as weather description and temperature.
Additional information: In addition, the user can get additional information about the job, such as a description of its functions or capabilities.

The bot is a useful assistant for travelers, which provides information about places (hotels, restaurants, shops, interesting places of the city) and weather in different cities of Ukraine, and also helps to navigate on the map.

Creating bots in Python has become popular for several reasons:
Python is a high-level, general-purpose programming language known for its simplicity, clear syntax, and wide range of applications. It is widely used for web application development, scientific computing, artificial intelligence, data analysis, game development, and much more.
Easy to learn and use: Python has a readable syntax and simple structure that makes it ideal for beginners. This allows you to quickly develop and configure bots without much effort.
Broad capabilities: Python has a large number of libraries and frameworks that help developers create a variety of features for their bots. This includes libraries for working with social media APIs, natural language processing, building web interfaces, and more.
Support Telegram Bot API: Telegram provides an API that allows you to create bots for this platform. Python libraries such as telebot provide an easy way to interact with this API and develop functions for bots.
Active developer community: Python has a large and active developer community that provides support, resources, and advice. This makes the process of developing bots in Python more accessible and enjoyable.
Cross-platform: Python code can run on different operating systems, making bots more flexible and accessible to different users.

The following tools and libraries are used in the code

1. telebot (TeleBot):
    - Purpose: This is a library for working with the Telegram Bot API in Python.
Telegram bot (TeleBot) is a program that automates interaction with users through the Telegram messenger using the Telegram Bot API. Such a bot can send messages, interact with user commands, receive incoming messages, respond to them, react to events, and more.
    - Functionality: Allows you to create, configure and manage bots in Telegram, including processing incoming messages, sending messages to users and creating keyboards to interact with them.
    - Usage in code: The library is imported using `import telebot` and the bot itself is created using `telebot.TeleBot(TOKEN)`.
An API (Application Programming Interface) is a set of rules and protocols that define how one software component interacts with another. An API defines which functions and operations one software component can use to communicate with other components or services
2. requests:
    - Purpose: This is a library for making HTTP requests in Python.
    - Functionality: Allows you to retrieve data from web servers using a variety of request methods such as GET, POST, PUT, etc.
    - Usage in code: Used to retrieve weather data from an external API using HTTP requests.
3. types with telebot:
    - Purpose: This is a module for using Telegram message types in the telebot library.
    - Functionality: Allows you to create a variety of message types, including keyboards, stickers, media files, and more.
    - Usage in code: Used to create keyboards for user interaction and other objects such as buttons.
4. api.openweathermap.org:
    - Purpose: This is a web API for getting weather information.
    - Functionality: Provides access to up-to-date weather data in various locations around the world.
    - Usage in code: Used to get information about the weather in different cities so that the bot can inform users about the current weather conditions.
WEATHER_API_KEY is a variable containing the weather API access key used to retrieve weather information from an external service. An API key is a unique identifier that is provided when registering with a service that provides an API. This is usually necessary to authenticate requests to the service and gain access to its functionality.

5. set():
    - Purpose: This is a data structure in Python that represents an unordered collection of unique elements.
    - Functionality: It is used to store unique chat IDs so that the bot can send messages to many users at the same time.
    - Usage in code: Used to store chat IDs of users to send messages to.
6. Places_data is a dictionary in the used code, which contains data about different places in different cities of Ukraine. This dictionary contains information about hotels, restaurants, shops and places of interest in cities such as Kyiv, Odesa, Kharkiv, Vinnytsia, Lviv and Uzhhorod.

The code uses a map to display locations in different cities of Ukraine. The code uses the bot.send_location() function, which allows users to send the coordinates of a location on a map.

Here's how this feature works:
You call the bot.send_location() function with parameters chat_id, latitude and longitude.
chat_id is the unique ID of the chat or user you want to send the location to.
latitude and longitude are the coordinates of the place you want to show on the map. The latitude coordinate indicates north or south latitude, and the longitude coordinate indicates east or west longitude.
Example: bot.send_location(chat_id, latitude=49.8397, longitude=24.0297)
In this example, latitude=49.8397 and longitude=24.0297 are responsible for the coordinates of the location in Lviv. After calling this function, the user will receive a message with the location, which will be displayed on the map in his chat with the bot.






















