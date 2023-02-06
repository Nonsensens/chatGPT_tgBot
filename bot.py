from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from gpt import ask_gpt


bot = Bot(token='{GITHUB_TOKEN_TG}')
storage = MemoryStorage()


dp = Dispatcher(bot, storage=storage)


@dp.register_message_handler
async def gpt_bot(message: types.Message):
    await message.answer(ask_gpt(message.text))

if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True, timeout=5, loop=True)