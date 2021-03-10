import os

from dotenv import load_dotenv

load_dotenv()

# токен для бота
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

# список админов бота
admins = [
    227718654,
]

# каналы для бота
channels = [

]
ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}