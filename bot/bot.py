import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, FSInputFile
from pathlib import Path

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# ЗАМЕНИТЕ ЭТОТ ТОКЕН НА ВАШ НАСТОЯЩИЙ ТОКЕН!
API_TOKEN = '8584211770:AAGFGh_F1eV3reHHO3SSfr3kiEDZgyIDTzo'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Кнопки
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='кошка')],
        [KeyboardButton(text='мышь')],
        [KeyboardButton(text='пес')],
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Выберите кнопку для озвучки:", reply_markup=keyboard)

@dp.message(lambda msg: msg.text.lower() == "кошка")
async def cat_sound(message: types.Message):
    try:
        # Проверка существования файлов
        cat_img_path = Path('media/cat.webp')
        cat_audio_path = Path('media/cat.mp3')
        
        if not cat_img_path.exists():
            await message.answer(f"Файл {cat_img_path} не найден")
            return
        if not cat_audio_path.exists():
            await message.answer(f"Файл {cat_audio_path} не найден")
            return
            
        cat_img = FSInputFile(cat_img_path)
        cat_audio = FSInputFile(cat_audio_path)
        
        await message.answer_photo(cat_img, caption="Кошка")
        await message.answer_voice(cat_audio)
        
    except Exception as e:
        await message.answer(f"Ошибка: {str(e)}")
        logging.error(f"Ошибка в cat_sound: {e}")

@dp.message(lambda msg: msg.text.lower() == "пес")
async def dog_sound(message: types.Message):
    try:
        dog_img_path = Path('media/dog.webp')
        dog_audio_path = Path('media/dog.mp3')
        
        if not dog_img_path.exists():
            await message.answer(f"Файл {dog_img_path} не найден")
            return
        if not dog_audio_path.exists():
            await message.answer(f"Файл {dog_audio_path} не найден")
            return
            
        dog_img = FSInputFile(dog_img_path)
        dog_audio = FSInputFile(dog_audio_path)
        
        await message.answer_photo(dog_img, caption="Пес")
        await message.answer_voice(dog_audio)
        
    except Exception as e:
        await message.answer(f"Ошибка: {str(e)}")
        logging.error(f"Ошибка в dog_sound: {e}")

@dp.message(lambda msg: msg.text.lower() == "мышь")
async def mouse_sound(message: types.Message):
    try:
        mouse_img_path = Path('media/mouse.jpg')
        mouse_audio_path = Path('media/mouse.mp3')
        
        if not mouse_img_path.exists():
            await message.answer(f"Файл {mouse_img_path} не найден")
            return
        if not mouse_audio_path.exists():
            await message.answer(f"Файл {mouse_audio_path} не найден")
            return
            
        mouse_img = FSInputFile(mouse_img_path)
        mouse_audio = FSInputFile(mouse_audio_path)
        
        await message.answer_photo(mouse_img, caption="Мышь")
        await message.answer_voice(mouse_audio)
        
    except Exception as e:
        await message.answer(f"Ошибка: {str(e)}")
        logging.error(f"Ошибка в mouse_sound: {e}")

# Обработчик для всех сообщений (для отладки)
@dp.message()
async def echo(message: types.Message):
    logging.info(f"Получено сообщение: {message.text}")
    await message.answer(f"Вы написали: '{message.text}'. Используйте кнопки ниже.")

async def main():
    logging.info("Бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())