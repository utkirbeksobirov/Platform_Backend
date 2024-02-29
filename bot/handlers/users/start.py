from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from loader import dp
from save import save_user, activate_user
import json
from aiogram import types


text_info = """
Assalomu alaykum! NOXONFX UZ botga xush kelibsiz!
Keling sizni xizmatlarimiz bilan tanishtiraman.

Product va Servislar

Product va Servislarimiz haqida batafsil ma'lumot olish uchun pastdagi havolani bosing 👇

https://www.noxonfx.com/

Bog'lanish

Toshkent Filial: +998 95 9 80 51 11
Farg'ona  Filial: +998 95 016 69 68
Toshkent   ICT: +998 90 965 69 96

To'lov qilib /kirish ni bosib kirish kodini oling va platformaga kiring.
"""


@dp.message_handler(Command('start'))
async def show_menu1(message: Message):
    usr = save_user(message)
    if usr.status_code == 201:
        await message.reply(text_info, parse_mode=types.ParseMode.MARKDOWN)
    else:
        await message.reply(f"Ushbu hisob allaqachon yaratilgan. \n\n{text_info}", parse_mode=types.ParseMode.MARKDOWN)


@dp.message_handler(Command('kirish'))
async def show_menu2(message: Message):
    usr = activate_user(message.from_user.id)
    if usr.status_code == 200:
        # usr_txt = json.loads(usr.text)
        await message.reply(f"<b>Kod:</b> {usr.text}")
    elif usr.status_code == 400:
        # usr_txt = json.loads(usr.text)
        await message.reply(usr.text)
    else:
        # usr_txt = json.loads(usr.text)
        await message.reply(f"<b>Xolat:</b> siz to'lov qilmagansiz!")
    # await message.reply(f"{usr.text}")
