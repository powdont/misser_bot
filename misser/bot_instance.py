from aiogram import Bot, types
from aiogram.client.default import DefaultBotProperties
from token_api import TOKEN_API

bot = Bot(
    TOKEN_API, 
    default=DefaultBotProperties(
        parse_mode='HTML',
    )
)