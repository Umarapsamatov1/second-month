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
# from keyboards import buttons_category
# from texno import pars_texno
#
# load_dotenv()
#
# TOKEN = os.getenv('TOKEN')
#
# bot = Bot(
#     TOKEN,
#     default=DefaultBotProperties(parse_mode='HTML')
# )
#
# dp = Dispatcher()
#
#
# @dp.message(Command('start'))
# async def command_start(message: Message):
#     full_name = message.from_user.full_name
#     await message.answer(f"Salom <b>{full_name}</b>\n"
#                          f"Texnomart* do'koniga hush kelibsiz 🥂")
#     await show_category_menu(message)
#
#
# async def show_category_menu(message: Message):
#     await message.answer("Bo'limlardan birini tanlang 👇", reply_markup=buttons_category())
#
#
# @dp.message()
# async def get_product_texno(message: Message):
#     category_text = message.text
#     category_key = get_values(category_text)
#
#     if category_key is None:
#         return await message.answer(
#             "Kechirasiz, bunday kategory mav jud emas\n"
#             "Quyidagi tugmalarnda birini tanlang 👇"
#         )
#     get_product = pars_texno(category_key)
#     if not get_product:
#         return await message.answer("Bunday kategory mavnud emas !")
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
#             caption=f"{title}\n\n{credit_price}\n\n<b>{price}</b>"
#         )
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())
#
