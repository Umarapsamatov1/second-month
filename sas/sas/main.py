# import os
# import shutil
# import uuid
#
# import yt_dlp
#
# from dotenv import load_dotenv
#
# from telegram import Update
# from telegram.ext import (
#     Updater,
#     CommandHandler,
#     MessageHandler,
#     Filters,
#     CallbackContext
# )
#
# load_dotenv()
#
# TOKEN = os.getenv("BOT_TOKEN")
#
# DOWNLOAD_FOLDER = "downloads"
#
# os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
#
#
# def start(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         "👋 Salom!\n\n"
#         "Instagram video yuklab beruvchi botman.\n\n"
#         "📥 Instagram Reel yoki Post linkini yuboring."
#     )
#
#
# def instagram_download(url):
#     random_name = str(uuid.uuid4())
#
#     folder = os.path.join(
#         DOWNLOAD_FOLDER,
#         random_name
#     )
#
#     os.makedirs(folder, exist_ok=True)
#
#     options = {
#         "format": "best",
#         "outtmpl": os.path.join(
#             folder,
#             "%(id)s.%(ext)s"
#         ),
#         "quiet": True,
#         "no_warnings": True
#     }
#
#     with yt_dlp.YoutubeDL(options) as ydl:
#         info = ydl.extract_info(
#             url,
#             download=True
#         )
#
#         file_path = ydl.prepare_filename(info)
#
#     return file_path, folder
#
#
# def download_video(
#         update: Update,
#         context: CallbackContext
# ):
#     url = update.message.text.strip()
#
#     # Instagram linkni tekshiramiz
#     if "instagram.com" not in url:
#         update.message.reply_text(
#             "❌ Instagram link yuboring."
#         )
#
#         return
#
#     loading_message = update.message.reply_text(
#         "⏳ Video yuklanmoqda..."
#     )
#
#     folder = None
#
#     try:
#
#         file_path, folder = instagram_download(url)
#
#         if not os.path.exists(file_path):
#             loading_message.edit_text(
#                 "❌ Video topilmadi."
#             )
#
#             return
#
#         with open(file_path, "rb") as video:
#
#             update.message.reply_video(
#                 video=video,
#                 caption="✅ Instagram video yuklandi"
#             )
#
#         loading_message.delete()
#
#
#     except Exception as error:
#
#         print("Xatolik:", error)
#
#         loading_message.edit_text(
#             "❌ Videoni yuklab bo'lmadi."
#         )
#
#
#     finally:
#
#         if folder and os.path.exists(folder):
#             shutil.rmtree(
#                 folder,
#                 ignore_errors=True
#             )
#
#
# def main():
#     updater = Updater(
#         TOKEN,
#         use_context=True
#     )
#
#
#     dispatcher = updater.dispatcher
#
#     # /start
#     dispatcher.add_handler(
#         CommandHandler(
#             "start",
#             start
#         )
#     )
#
#     # Oddiy text / Instagram link
#     dispatcher.add_handler(
#         MessageHandler(
#             Filters.text & ~Filters.command,
#             download_video
#         )
#     )
#     # Pass request arguments to increase connection timeouts
#
#     print("Bot ishga tushdi...")
#
#     updater.start_polling()
#
#     updater.idle()
#
#
# if __name__ == "__main__":
#     main()

# import asyncio
# import os
# import yt_dlp
# from aiogram import Bot, Dispatcher, F
# from aiogram.types import Message, FSInputFile
# from aiogram.filters import CommandStart
#
# BOT_TOKEN = "8685473654:AAErXHFoRTTAHJjMxfGj7-ciHsNifC89zdQ"
#
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()
#
#
# @dp.message(CommandStart())
# async def start_cmd(message: Message):
#     await message.answer("Salom! Menga Instagram Reel yoki video havolasini (link) yuboring.")
#
#
# @dp.message(F.text.contains("instagram.com"))
# async def download_instagram_video(message: Message):
#     wait_msg = await message.answer("Video yuklanmoqda, kuting...")
#
#     url = message.text.strip()
#     file_path = f"video_{message.message_id}.mp4"
#
#     ydl_opts = {
#         'outtmpl': file_path,
#         'quiet': True,
#         'no_warnings': True,
#     }
#
#     try:
#         # Videoni yuklab olish
#         loop = asyncio.get_running_loop()
#         await loop.run_in_executor(None, lambda: yt_dlp.YoutubeDL(ydl_opts).download([url]))
#
#         # Telegramga yuborish
#         if os.path.exists(file_path):
#             video_file = FSInputFile(file_path)
#             await message.answer_video(video=video_file, caption="Videongiz tayyor!")
#             await wait_msg.delete()
#         else:
#             await wait_msg.edit_text("Videoni yuklab bo'lmadi.")
#
#     except Exception as e:
#         print(f"Xatolik: {e}")
#         await wait_msg.edit_text(
#             "Videoni yuklab bo'lmadi. Havola to'g'riligini yoki post ochiq (public) ekanligini tekshiring.")
#
#     finally:
#         # Serverda faylni o'chirish
#         if os.path.exists(file_path):
#             os.remove(file_path)
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())













# import  asyncio
# import os
# import yt_dlp
# from aiogram import Bot,Dispatcher,F
# from aiogram.types import Message, FSInputFile
# from aiogram.filters import CommandStart
#
# TOKEN = '8685473654:AAErXHFoRTTAHJjMxfGj7-ciHsNifC89zdQ'
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
#
# @dp.message(CommandStart())
# async def start(message: Message):
#     await message.answer("assalomu alaykum botga xush kelibsiz ")
#
# @dp.message(F.text.contains("instagram.com"))
# async def instagram(message: Message):
#      wait_msg=await message.answer("video yuklanmoda kuting")
#      url=message.text.strip()
#      file_path=f"video_{message.message_id}.mp4"
#      ydl_opts={
#          "outtmpl": file_path,
#          "quiet": True,
#          "no_warnings": True,
#      }
#      try:
#          loop=asyncio.get_running_loop()
#          await loop.run_in_executor(None, lambda: yt_dlp.YoutubeDL(ydl_opts).download([url]))
#          if os.path.exists(file_path):
#           video_file = FSInputFile(file_path)
#           await message.answer_video(video=video_file,caption="video muvaffaqiyatli ravishda yuklab olindi !")
#           await wait_msg.delete()
#          else:
#              await wait_msg.edit_text("videoni yuklab bolmadi oka.")
#      except Exception as e:
#          print(f"xatolik {e}")
#          await wait_msg.edit_text(""
#                                   "linkni yuborishda yoki video public (xamma uchun ekanligini) tekshiring)")
#      finally:
#          if os.path.exists(file_path):
#              os.remove(file_path)
#
# async def main():
#     await dp.start_polling(bot)
#
# if __name__ == '__main__':
#     asyncio.run(main())







import os
import asyncio
import yt_dlp
# from aiogram import Bot,Dispatcher,F
# from aiogram.types import Message, FSInputFile
# from aiogram.filters import CommandStart

# TOKEN='8685473654:AAHsChUKFEb91ER-SgiiFZkgDfvNnBblp6M'
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
#
# @dp.message(CommandStart())
# async def start(message: Message):
#   # full_name = message.from_user.full_name
#    await message.answer("assalomu alaykum  instagramdan video yuklovchi botga xush kelibsiz video yulash uchun link yuboring")
# @dp.message(F.text.contains('instagram.com'))
# async def instagram(message: Message):
#    wait_msg= await message.answer("video yuklnamoqda biroz kutib turing")
#    url = message.text.strip()
#    file_path=f"video_{message.message_id}.mp4"
#    ydl_opts = {
#        "outtmpl": file_path,
#        "quiet": True,
#        "no_warnings": True,
#      }
#    try:
#                     loop=asyncio.get_running_loop()
#                     await loop.run_in_executor(None, lambda: yt_dlp.YoutubeDL(ydl_opts).download([url]))
#                     if os.path.exists(file_path):
#                      video_file=FSInputFile(file_path)
#                      await message.answer_video(video=video_file, caption="video muvaffaqiyatli yuklav olindi")
#                      await wait_msg.delete()
#                     else:
#                         await wait_msg.edit_text("videoni yuklab bolmadi oka")
#    except Exception as e:
#        print(f"xato bob qoldi oka {e}")
#        await wait_msg.edit_text("videoni linkini togriligiga va video public ejnaligigiga ishonch hosil qiling ")
#    finally:
#        if os.path.exists(file_path):
#            os.remove(file_path)
# async def main():
#    await dp.start_polling(bot)
# if __name__ == '__main__':
#     asyncio.run(main())
#

