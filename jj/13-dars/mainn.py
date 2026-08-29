# import asyncio
# import time
#
# from aiogram.client.default import DefaultBotProperties
# from aiogram import Bot, Dispatcher
# from aiogram.types import Message
# from dotenv import load_dotenv
# import os
# from aiogram.filters import Command
#
# from config import get_values
# from buttons import get_keyboard
# from main import pars_texno
#
# load_dotenv()
#
# TOKEN=os.getenv("TOKEN")
#
# bot=Bot(
#     TOKEN,
#     default=DefaultBotProperties(parse_mode="html")
# )
# dp=Dispatcher()
#
# @dp.message(Command("start"))
# async def command_start(message:Message):
#     full_name=message.from_user.full_name
#     await message.answer(f"salom <b>{full_name}</b> botga\n"
#                          f"xush kelibsiz"
#
#     )
#     await show_category_menu(message)
#
# async def show_category_menu(message:Message):
#     await message.answer("bolimlardan birini tanla", reply_markup=get_keyboard())
#
# @dp.message()
# async def get_product_texno (message:Message):
#     category_text=message.text
#     category_key=get_values(category_text)
#     if category_key is None:
#         return await message.answer(f"malumot topilmadi")
#
#     get_product=pars_texno(category_text)
#     if not get_product:
#         return await message.answer(f"bunday kategoriya yoq !")
#     for product in get_product:
#         image=product.get("images")
#         title = product.get("title")
#         credit_price = product.get("credit_price")
#         price = product.get("price")
#
#         time.sleep(0.5)
#
#         await message.answer_photo(
#            photo=image,
#            caption=f"{title}\n\n {credit_price}\n\n {price}",)
# async def main():
#     await dp.start_polling(bot)
#
# if __name__ == '__main__':
#     asyncio.run(main())









import asyncio
import time

from aiogram.client.default import DefaultBotProperties
from aiogram import Bot,Dispatcher
from aiogram.types import Message
from dotenv import load_dotenv
import os
from aiogram.filters import Command

from config import get_values
from buttons import get_keyboard
from main import pars_texno
load_dotenv()
TOKEN=os.getenv("TOKEN")

bot=Bot(TOKEN,
        default=DefaultBotProperties(parse_mode='html')




        )

dp=Dispatcher()

@dp.message(Command("start"))
async def start(message:Message):
    full_name=message.from_user.full_name
    await message.answer(f"assalomu alayku {full_name}, botga xush kelibsiz")
    await show_category_menu(message)

async def show_category_menu(message:Message):
    await message.answer("bolimlardan birini tanlang"
                         )

@dp.message()
async def get_product_texno(message:Message):
    messages=message.text
    message_get=get_values(messages)
    if message_get is None:
        await message.answer("malumot topilmadi")
    lek=pars_texno(message_get)
    if not message_get :
        return await message.answer("bunday kategoriya topilmadi")
    for product in lek:
         image=product.get("images")
         title = product.get("title")
         credit_price = product.get("credit_price")
         price = product.get("price")
         time.sleep(0.5)

         await message.answer.photo(
             photo=image,
             caption=f"{title}\n\n{credit_price}\n\n{price}",
         )
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())