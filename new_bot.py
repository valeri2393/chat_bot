# 1.Импорт библиотек
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message             # ловим все обновления этого типа 
from aiogram.filters.command import Command   # обрабатываем команды /start, /help и другие


# logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='bot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

translit_rules = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
    'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
    'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
    'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': 'ie', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'iu',
    'я': 'ia', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
    'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH',
    'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ъ': 'IE', 'Ы': 'Y', 'Ь': '', 'Э': 'E',
    'Ю': 'IU', 'Я': 'IA'
}

# Обработ команды /start
@dp.message(Command(commands=['start']))
async def start(message: Message):
    await message.reply("Привет! Отправьте мне ваше ФИО на русском языке, и я переведу его на латиницу в соответствии с Приказом МИД России от 12.02.2020 № 2113.")

# Функция для перевода ФИО
def transliterate_fio(text):
    result = ''
    for char in text:
        if char in translit_rules:
            result += translit_rules[char]
        else:
            result += char
    return result

# Обработ текст сообщений
@dp.message()
async def translit_fio(message: Message):
    fio = message.text                      #ФИО от пользователя
    translit_fio = transliterate_fio(fio)   #Транслитерация ФИО
    await message.reply(translit_fio)       #Отправляем ФИО пользователю

    # Логируем полученное ФИО и его транслитерацию
    logging.info(f'Пользователь {message.from_user.username} отправил ФИО: {fio}, транслитерация: {translit_fio}')

# Запускаем бота
if __name__ == '__main__':
    dp.run_polling(bot)