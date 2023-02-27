from aiogram import types
from loader import dp

@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'Твой id: {message.from_user.id} \n\n'

                         f'1. Отправь картинку файлом\n'
                         f'2. Нажми кнопку "1" или "2" в зависимости от типа обрезки картинки\n'
                         f'3. Получи готовую картинку файлом', reply_markup=types.ReplyKeyboardRemove())
