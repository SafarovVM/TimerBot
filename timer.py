import asyncio
import datetime
import logging
import time

from aiogram import Bot, Dispatcher, types
from aiogram.utils import exceptions, executor

logging.basicConfig(level=logging.INFO)


API_TOKEN = 'ВАШ ТОКЕН'


COUNTDOWN_DATE = datetime.datetime(2023, 4, 14, 14, 00, 0)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    try:

        remaining_time = COUNTDOWN_DATE - datetime.datetime.now()
        days, seconds = remaining_time.days, remaining_time.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60


        keyboard = types.InlineKeyboardMarkup()
        countdown_button = types.InlineKeyboardButton(
            text=f'{days} дней {hours} часов {minutes} минут {seconds} секунд',
            callback_data='countdown'
        )
        keyboard.add(countdown_button)


        await message.answer('TEHNIKUM DIGITAL HACKATHON 2023', reply_markup=keyboard)
    except exceptions.TelegramAPIError as error:
        logging.exception(error)



@dp.callback_query_handler(lambda callback_query: callback_query.data == 'countdown')
async def countdown_handler(callback_query: types.CallbackQuery):
    try:
        while True:

            remaining_time = COUNTDOWN_DATE - datetime.datetime.now()
            days, seconds = remaining_time.days, remaining_time.seconds
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60


            keyboard = types.InlineKeyboardMarkup()
            countdown_button = types.InlineKeyboardButton(
                text=f'{days} дней {hours} часов {minutes} минут {seconds} секунд',
                callback_data='countdown'
            )
            keyboard.add(countdown_button)

            await callback_query.message.edit_reply_markup(
                reply_markup=keyboard
            )
            time.sleep(60)

    except exceptions.TelegramAPIError as error:
        logging.exception(error)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
