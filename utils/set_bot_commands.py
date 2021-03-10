# команды для бота вызываемые /! символами
from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запуск бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("show_village", "Узнать два ближайших поселка"),
    ])
