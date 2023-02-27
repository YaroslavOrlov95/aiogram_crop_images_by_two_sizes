async def on_startup(dp):

    import Filters
    Filters.setup(dp)

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands

    await set_default_commands(dp)

    print('Бот запущен')

if __name__ == '__main__':
    from aiogram.utils import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)