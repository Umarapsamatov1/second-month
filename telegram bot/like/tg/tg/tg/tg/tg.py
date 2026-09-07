# from telegram import(Update,InlineKeyboardButton,InlineKeyboardMarkup)
# from telegram.ext import(
# Updater,
# CommandHandler,
# MessageHandler,
# filters,
# CallbackQueryHandler,
# CallbackContext,
# ConversationHandler)
# import sqlite3
# TOKEN='8842994433:AAHecsvcKmnB-MBHgII9Nec-pWhSSrrV0Dg'
# ADMIN_ID=8593523279
#
#
# db = sqlite3.connect("movies.db", check_same_thread=False)
# cursor = db.cursor()
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS movies (
#     code TEXT PRIMARY KEY,
#     file_id TEXT,
#     captions TEXT
# )
# """)
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS channels (
#     channel TEXT PRIMARY KEY
# )
# """)
# db.commit()
# def get_channels():
#     cursor.execute("SELECT channel FROM channels")
#     return [i[0] for i in cursor.fetchall()]
#
#
# def check_subscription(bot, user_id):
#     channels = get_channels()
#     if not channels:
#         return True
#
#     for channel in channels:
#         try:
#             member = bot.get_chat_member(channel, user_id)
#             if member.status in ['left', 'kicked']:
#                 return False
#         except:
#             return False
#     return True
# def subscription_keyboard():
#     keyboard = []
#
#     for ch in get_channels():
#         if ch.startswith("@"):
#             url = f"https://t.me/{ch[1:]}"
#         else:
#             url = ch
#
#         keyboard.append([
#             InlineKeyboardButton(f"{ch}", url=url)
#         ])
#
#     keyboard.append([
#         InlineKeyboardButton("Tekshirish", callback_data='check_sub')
#     ])
#     return InlineKeyboardMarkup(keyboard)
#
# def start(update: Update, context: CallbackContext):
#     user_id = update.message.from_user.id
#
#     if not check_subscription(context.bot, user_id):
#         update.message.reply_text("Botdan foydalanish kanallarga obuna bo'ling !",
#                                   reply_markup=subscription_keyboard())
#         return
#
#     update.message.reply_text("Assalomu Alaykum\n"
#                               "Kino kodini kiriting: ")