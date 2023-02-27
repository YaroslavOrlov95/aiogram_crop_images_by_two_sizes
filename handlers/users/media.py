import os

import PIL
from aiogram import types
from aiogram.types import ContentType, Message, InputFile, MediaGroup, InputMediaPhoto
from PIL import Image, ImageFilter
from loader import dp, bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from states import register
from keyboards.inline_kb import ikb_menu_
from aiogram.dispatcher import FSMContext
from data.config import BOT_TOKEN
# from dotenv import load_dotenv
import re
from aiogram.types import InputFile
from io import BytesIO
from aiogram.types import CallbackQuery

dict_ = {}
list_name =[]

@dp.message_handler(content_types=ContentType.DOCUMENT)
async def edit(msg: types.Message, state: FSMContext):
    async with state.proxy() as edits_photo:
        chat_id = msg.from_user.id
        a = msg.document.file_id
        b = msg.document
        name_file_with_format = b.file_name
        edits_photo["photo"] = msg.document.file_id
        file_id = edits_photo["photo"]

        k = (await bot.download_file_by_id(file_id))

        list_split_format = name_file_with_format.split(r'.')
        name_file = list_split_format[0]
        list_name.append(name_file)

        img = Image.open(k)
        img.thumbnail(size=(1240,1754))


        x = (0, 451, 1230, 1751)
        y = (0, 207, 1240, 1751)

        kak_1 = img.crop(x)
        kak_2 = img.crop(y)

        dict_['obj1'] = kak_1
        dict_['obj2'] = kak_2

        await dp.bot.send_document(chat_id=chat_id, document=a,
                                   reply_markup=ikb_menu_)

        await register.test1.set()

@dp.callback_query_handler(lambda c: c.data == '1', state=register.test1)
async def send_photo(message : types.message, state: FSMContext):
    chat_id = message.from_user.id
    print(chat_id)

    bio = BytesIO()

    print(dict_)
    print(list_name)

    bio.name = f'{list_name[0]}.jpg'
    dict_['obj1'].save(bio, 'JPEG')
    bio.seek(0)

    dict_.clear()
    list_name.clear()
    print(dict_)
    print(list_name)
    await dp.bot.send_document(chat_id=chat_id, document=bio)
    await state.finish()

@dp.callback_query_handler(lambda c: c.data == '2', state=register.test1)
async def send_photo(message : types.message, state: FSMContext):
    chat_id = message.from_user.id
    print(chat_id)

    bio = BytesIO()

    print(dict_)
    print(list_name)

    bio.name = f'{list_name[0]}.jpg'
    dict_['obj2'].save(bio, 'JPEG')
    bio.seek(0)



    dict_.clear()
    list_name.clear()
    print(dict_)
    print(list_name)
    await dp.bot.send_document(chat_id=chat_id, document=bio)
    await state.finish()