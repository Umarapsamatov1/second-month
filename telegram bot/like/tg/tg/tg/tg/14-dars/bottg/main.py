import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from dotenv import load_dotenv

from config import get_values
from keyboards import buttons_category
from parsing import pars_texno

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def command_start(message: types.Message):
    full_name = message.from_user.full_name
    await message.answer(f"Salom <b>{full_name}</b>\nAsaxiy do'koniga xush kelibsiz 🛒", parse_mode='HTML')
    await show_category_menu(message)


async def show_category_menu(message: types.Message):
    await message.answer("Bo'limlardan birini tanlang 👇", reply_markup=buttons_category())


@dp.message()
async def send_products_handler(message: types.Message):
    category_path = get_values(message.text)

    if category_path:
        await message.answer("🔍 Ma'lumotlar yuklanmoqda...")
        products = pars_texno(category_path)

        if not products:
            await message.answer("Mahsulot topilmadi.")
            return

        for item in products:
            caption = (
                f"<b>{item['title']}</b>\n\n"
                f"<b>Narxi:</b> {item['price']} so'm\n"
                f"<b>Muddatli to'lov:</b> {item['credit_price']}\n\n"
                f"🔗 <a href='{item['link']}'>Mahsulotni ko'rish</a>"
            )

            if item['images']:
                try:
                    await message.answer_photo(photo=item['images'], caption=caption, parse_mode='HTML')
                except Exception:
                    await message.answer(caption, parse_mode='HTML')
            else:
                await message.answer(caption, parse_mode='HTML')
    else:
        await message.answer("Iltimos, menyudagi tugmalardan birini tanlang!", reply_markup=buttons_category())


async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())