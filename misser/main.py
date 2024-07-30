import asyncio
from aiogram import types, Dispatcher, Bot
from aiogram.filters import CommandStart
from aiogram.utils import markdown
from token_api import TOKEN_API
from bot_instance import bot
from bot.handlers.user_handlers import user_router



#@dp.message(CommandStart())
#async def cmd_start(msg: types.Message) -> None:
#    reply_text = f'Hello,  {markdown.hbold(msg.from_user.first_name)}'
#    await msg.answer(text=reply_text)

def register_routers(dp: Dispatcher) -> None:
    """Registers routers"""

    dp.include_router(user_router)


async def main() -> None:
    """The main function which will execute our event loop and start polling."""
    dp = Dispatcher()

    register_routers(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())