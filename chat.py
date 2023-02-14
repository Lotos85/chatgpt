import openai 
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from aiogram import executor

bot = Bot(token="5893397062:AAFSKxEGVxCzX7yHS_P_FkvY00u1NiPepos")
dp = Dispatcher(bot)
openai.api_key = "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"


@dp.message_handler(Command(commands=["start"]))
async def start(message: Message) -> None:
    await message.answer("Пртвет!\n Я бот - искусственный интеллект")
    return

  
@dp.message_handler(Command(commands=["chat"]))
async def ii(message: Message) -> None:
    message.text[6:]
    response = openai.Completion.create( 
     engine="text-davinci-003", 
     prompt='"""\n{}\n"""'.format(message.text), 
     temperature=0, 
     max_tokens=1200, 
     top_p=1, 
     frequency_penalty=0, 
     presence_penalty=0, 
     stop=['"""'])
    await bot.send_message(message.chat.id, f'\n{response["choices"][0]["text"]}', parse_mode='Markdown')
    return
    

executor.start_polling(dp, skip_updates=True)

