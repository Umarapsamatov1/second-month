from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import CATEGORIES

def get_keyboard():
    buttons=[]
    for category in CATEGORIES.keys():
        buttons.append([KeyboardButton(text=category)])

        markup = ReplyKeyboardMarkup(
            keyboard=buttons,
            resize_Keyboard=True,
            one_time_Keyboard=False,

        )
        return markup