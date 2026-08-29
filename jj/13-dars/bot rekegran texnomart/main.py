import asyncio
import time

from aiogram.client.default import DefaultBotProperties
from aiogram import Bot,Dispatcher
from aiogram.types import Message
from dotenv import load_dotenv
import os
# from aiogram.filters import Command
#
# from config import get_values
# from buttons import get_keyboard
# from parsing import pars_texno
#
# load_dotenv()
#
# TOKEN=os.getenv("TOKEN")
#
# bot=Bot(
#     TOKEN,
#     default=DefaultBotProperties(parse_mode="html")
#
# )
# dp=Dispatcher()
# @dp.message(Command("start"))
# async  def start(message:Message):
#     full_name=message.from_user.full_name
#     await message.answer(f"salom <b>{full_name}</b>\n"
#                          f"texnomart dokoni botiga xush kelibsiz")
#     await show_category_menu(message)
#
# async def show_category_menu(message:Message):
#     await message.answer("quyidagi bolimlardan birini tanlang ", Reply_Markup=get_keyboard())
#
# @dp.message()
# async def get_product_texno(message:Message):
#     category_text=message.text
#     catgeory_key=get_values(category_text)
#
#     if catgeory_key is None:
#         return await message.answer("kechirasiz bunday tugma yo'q\n"
#                                     "quyidagilaridan birini tanlang")
#
#     get_product=pars_texno(catgeory_key)
#     if not get_product:
#         return await message.answer("kechasiz bunday kategoriya yo'q")
#
#     for product in get_product:
#         image = product.get('images')
#         title = product.get('title')
#         credit_price = product.get('credit_price')
#         price = product.get('price')
#
#         time.sleep(0.5)
#
#         await message.answer_photo(
#             photo=image,
#             caption=f"{title}\n\n{credit_price}\n\n{price}"
#         )
#
# async def main():
#     await dp.start_polling()
#
# if __name__ == "__main__":
#     asyncio.run(main())
#
