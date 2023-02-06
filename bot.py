from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from gpt import askGPT


bot = Bot(token='5789988431:AAHxw4AsAX5o_td7UaVKSkSm6kYi8wMBU4U')
storage = MemoryStorage()


dp = Dispatcher(bot, storage=storage)


@dp.register_message_handler
async def gpt_bot(message: types.Message):
    await message.answer(askGPT(message.text))

if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True, timeout=5, loop=True)