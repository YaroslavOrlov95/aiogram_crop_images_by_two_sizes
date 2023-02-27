from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu_ = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='1', callback_data='1'),
                                        InlineKeyboardButton(text='2', callback_data='2')
                                    ],
                                ])