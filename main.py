from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = '6091700098:AAFqdYEWfHbu00igPFgtoF_HZYH4XbyW_Z8'

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "Who is president of Russia?"
    answers = [
        "Putin",
        "Obama",
        "Trump",
        "Japarov",
        "Macron",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Да, именно он",
        open_period=10,
        reply_markup=markup
    )
@dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
        markup = InlineKeyboardMarkup()
        button_1 = InlineKeyboardButton("NEXT", callback_data="button_2")
        markup.add(button_1)

        question = "Кого я люблю?"
        answers = [
            "Лера",
            "Айзирек",
            "Амина",
            "Алия",
            "Кайрат",
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

@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo = open('Загрузки/mem.png', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=message.text)
    print(message)






if __name__ == "main":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

