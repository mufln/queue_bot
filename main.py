import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message
from cfg import *
bot = Bot(token=BOT_TOKEN)
r = Router()
dp = Dispatcher()
dp.include_router(r)
queue = []


@r.message(Command("start"))
async def start(message: Message):
    await message.reply("Hello!")


@r.message(Command('enqueue'))
async def enqueue(message: Message):
    if not message.from_user.id in queue:
        queue.append(message.from_user.id)
        await message.answer("Ты добавлен в очередь")
        if len(queue) == 1:
            await message.answer("Ты идешь первым!")
    else:
        await message.answer("Уже в очереди")


@r.message(Command('dequeue'))
async def dequeue(message: Message):
    if len(queue) > 0:
        if queue[0] == message.from_user.id:
            await message.reply(f"Ты удален из очереди")
            queue.pop(0)
            await message.bot.send_message(queue[0], "Твоя очередь")
        elif message.from_user.id in queue:
            await message.reply(f"Ты удален из очереди")
            queue.remove(message.from_user.id)
    else:
        await message.answer("Очередь пуста")

@r.message(Command("purge"))
async def purge(message: Message):
    queue.clear()
    await message.answer("Очередь очищена")


@r.message(Command("queue"))
async def listqueue(message: Message):
    if message.from_user.id in queue:
        await message.answer(f"Твоя очередь: {queue.index(message.from_user.id)+1}")
    else:
        await message.answer(f"Ты не в очереди")


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())