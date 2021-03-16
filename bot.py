#!venv/bin/python
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import BotBlocked
from aiogram.dispatcher.filters import Text
from os import getenv
from sys import exit


# Получаем BOT_TOKEN из окружения (getenv form module os)
BOT_TOKEN = getenv("BOT_TOKEN")
if not BOT_TOKEN:
    exit("Error: no token provided")

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Хэндлер на команду /start
@dp.message_handler(commands='start')
async def cmd_start(massage: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("М ♂", "Ж ♀")
    # Приветствуем, предлагаем выбрать пол (отправляем клаву)
    await massage.answer(text="Привет.\nПрежде чем начать общение, выбери свой пол.",
                         reply_markup=keyboard)

# Хэндлер
@dp.message_handler(Text(equals="М ♂"))
async def define_man(massage: types.Message):
    await massage.answer(text='Ок, М', reply_markup=types.ReplyKeyboardRemove())

# Хэндлер
@dp.message_handler(Text(equals="Ж ♀"))
async def define_woman(massage: types.Message):
    await massage.answer(text='Ок, Ж', reply_markup=types.ReplyKeyboardRemove())



@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True

id_last_user = 472890755

'''
@dp.message_handler()
async def answer_user(massage: types.Message):
    global id_last_user
    if id_last_user != massage.from_user.id:
        await bot.send_message(chat_id=id_last_user, text=massage.text)
    else:
        await massage.answer("Это сообщение не будет доставленно\n"
                             "Соблюдайте очередность, дождитесь ответа")

    id_last_user = massage.from_user.id
    print(id_last_user)
'''



if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)

#@dp.message_handler()
#async def echo(message: types.Message):
#    await message.answer(f"Message: {message.text}\n"+"from "
#                         f"{message.from_user['first_name']},"
#                         f" id: {message.from_user['id']}")
#    print("Отработал обработчик",
#          f"Message: {message.text}",
#          "from",
#          f"{message.from_user['first_name']}, id: {message.from_user['id']}")