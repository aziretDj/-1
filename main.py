from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
import logging
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f"Рад приветсвовать! {message.from_user.full_name}"
    )

@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open('media/мем-1.jpg','rb')
    await bot.send_photo(message.chat.id, photo=photo)

@dp.message_handler(commands='quiz')
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = 'Где проходил Чемпионат Мира по Футболлу 2022?'
    answers = [
        'Бразилия'
        'Катар'
        'Россия'
        'Уругвай'
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Стыдно не знать",
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_2")
    markup.add(button_1)

    question = "Сколько дней в году?"
    answers = [
        "123",
        "365",
        "666",
        "32",
        "БЕССКОНЕЧНОСТЬ",
        "-3",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Стыдно не знать",
        open_period=10,
        reply_markup=markup
    )

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=message.text)
    print(message)

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(message.chat.id,int(message.text) * int(message.text))
    else:
        await bot.send_message(message.from_user.id, message.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
