from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsPrivate(BoundFilter):
    async def check(self, message: types.message):
        return message.chat.type == types.ChatType.PRIVATE
