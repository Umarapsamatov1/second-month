from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from config import CATEGORIES

def get_keyboard():
    buttonss=[]
    for category in CATEGORIES.keys():
        buttonss.append([KeyboardButton(text=category)])

    markup=(ReplyKeyboardMarkup(
        keyboard=buttonss,
        resize_keyboard=True,
        one_time_keyboard=False,
    ))
    return markup
