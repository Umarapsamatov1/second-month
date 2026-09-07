# import os
# import shutil
# import uuid
# import asyncio
# import glob
#
# import yt_dlp
# from dotenv import load_dotenv
#
# from telegram import Update
# from telegram.ext import (
#     ApplicationBuilder,
#     CommandHandler,
#     MessageHandler,
#     filters,
#     ContextTypes,
# )
#
#
# # =========================
# # SOZLAMALAR
# # =========================
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
# # =========================
# # START BUYRUG'I
# # =========================
#
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#
#     await update.message.reply_text(
#         "👋 Salom!\n\n"
#         "Instagramdan video yuklab beruvchi botman.\n\n"
#         "📥 Instagram Reel yoki Post linkini yuboring."
#     )
#
#
# # =========================
# # INSTAGRAMDAN VIDEO YUKLASH
# # =========================
#
# def instagram_download(url):
#
#     # Har bir yuklama uchun alohida papka
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
#         # MP4 formatni tanlash
#         "format": "best[ext=mp4]/best",
#
#         # Fayl nomi
#         "outtmpl": os.path.join(
#             folder,
#             "video.%(ext)s"
#         ),
#
#         # Terminalda ortiqcha ma'lumot chiqarmaydi
#         "quiet": True,
#         "no_warnings": True,
#
#         # Internet kutish vaqti
#         "socket_timeout": 120,
#
#         # Qayta urinish
#         "retries": 20,
#         "fragment_retries": 20,
#
#         # HTTPS uchun
#         "nocheckcertificate": True,
#
#         # Agar kerak bo'lsa davom ettiradi
#         "continuedl": True,
#
#         # MP4 ga birlashtirish
#         "merge_output_format": "mp4",
#     }
#
#     try:
#
#         with yt_dlp.YoutubeDL(options) as ydl:
#
#             # Videoni yuklaymiz
#             info = ydl.extract_info(
#                 url,
#                 download=True
#             )
#
#             # Yuklangan fayl yo'lini aniqlaymiz
#             file_path = ydl.prepare_filename(info)
#
#         # Ba'zi hollarda yt-dlp fayl extensionini o'zgartirishi mumkin.
#         # Shuning uchun papkadagi videoni qidiramiz.
#
#         if not os.path.exists(file_path):
#
#             video_files = glob.glob(
#                 os.path.join(folder, "*")
#             )
#
#             for file in video_files:
#
#                 if file.lower().endswith(
#                     (".mp4", ".mkv", ".webm", ".mov")
#                 ):
#                     file_path = file
#                     break
#
#         return file_path, folder
#
#     except Exception:
#
#         # Xatolik bo'lsa papkani o'chirish uchun
#         # yuqoriga xatolikni yuboramiz
#         raise
#
#
# # =========================
# # VIDEO QABUL QILISH
# # =========================
#
# async def download_video(
#     update: Update,
#     context: ContextTypes.DEFAULT_TYPE
# ):
#
#     # Foydalanuvchi yuborgan link
#     url = update.message.text.strip()
#
#     # Instagram link ekanligini tekshirish
#     if "instagram.com" not in url.lower():
#
#         await update.message.reply_text(
#             "❌ Instagram link yuboring."
#         )
#
#         return
#
#     # Yuklanmoqda xabari
#     loading_message = await update.message.reply_text(
#         "⏳ Video yuklanmoqda...\n\n"
#         "Iltimos, biroz kuting."
#     )
#
#     folder = None
#
#     try:
#
#         # yt-dlp sinxron ishlaydi.
#         # asyncio.to_thread() uni alohida thread'da ishlatadi.
#         #
#         # MUHIM:
#         # context.application.loop ishlatmaymiz.
#         file_path, folder = await asyncio.to_thread(
#             instagram_download,
#             url
#         )
#
#         # Fayl mavjudligini tekshirish
#         if not file_path or not os.path.exists(file_path):
#
#             await loading_message.edit_text(
#                 "❌ Video topilmadi."
#             )
#
#             return
#
#         # Telegramga video yuborish
#         await loading_message.edit_text(
#             "📤 Video Telegramga yuborilmoqda..."
#         )
#
#         with open(file_path, "rb") as video:
#
#             await update.message.reply_video(
#                 video=video,
#                 caption="✅ Instagram video yuklandi!"
#             )
#
#         # Yuklanmoqda xabarini o'chirish
#         await loading_message.delete()
#
#     except Exception as error:
#
#         # Xatoni terminalga chiqarish
#         print("Xatolik:", error)
#
#         try:
#
#             await loading_message.edit_text(
#                 "❌ Video yuklab bo'lmadi.\n\n"
#                 "Instagram linkini tekshiring va "
#                 "qaytadan urinib ko'ring."
#             )
#
#         except Exception:
#
#             pass
#
#     finally:
#
#         # Yuklangan vaqtinchalik papkani o'chirish
#         if folder and os.path.exists(folder):
#
#             shutil.rmtree(
#                 folder,
#                 ignore_errors=True
#             )
#
#
# # =========================
# # ERROR HANDLER
# # =========================
#
# async def error_handler(
#     update: object,
#     context: ContextTypes.DEFAULT_TYPE
# ):
#
#     print(
#         "Bot xatosi:",
#         context.error
#     )
#
#
# # =========================
# # BOTNI ISHGA TUSHIRISH
# # =========================
#
# def main():
#
#     if not TOKEN:
#
#         print(
#             "❌ BOT_TOKEN topilmadi!"
#         )
#
#         print(
#             "'.env' faylida BOT_TOKEN borligini tekshiring."
#         )
#
#         return
#
#     # Application yaratish
#     app = (
#         ApplicationBuilder()
#         .token(TOKEN)
#         .connect_timeout(60)
#         .read_timeout(60)
#         .write_timeout(120)
#         .pool_timeout(60)
#         .build()
#     )
#
#     # /start
#     app.add_handler(
#         CommandHandler(
#             "start",
#             start
#         )
#     )
#
#     # Oddiy text xabarlar
#     app.add_handler(
#         MessageHandler(
#             filters.TEXT & ~filters.COMMAND,
#             download_video
#         )
#     )
#
#     # Error handler
#     app.add_error_handler(
#         error_handler
#     )
#
#     print(
#         "🤖 Bot ishga tushdi..."
#     )
#
#     # Botni ishga tushirish
#     app.run_polling()
#
#
# # =========================
# # START
# # =========================
#
# if __name__ == "__main__":
#     main()
# import os
# import shutil
# import uuid
#
# import yt_dlp
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
# os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
#
#
# # =========================
# # START
# # =========================
#
# def start(update: Update, context: CallbackContext):
#
#     update.message.reply_text(
#         "👋 Salom!\n\n"
#         "Instagram yuklovchi botga xush kelibsiz.\n\n"
#         "📥 Reel yoki video yuklash uchun "
#         "Instagram linkini yuboring."
#     )
#
#
# # =========================
# # INSTAGRAM DOWNLOAD
# # =========================
#
# def instagram_download(url):
#
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
#         "format": "best[ext=mp4]/best",
#
#         "outtmpl": os.path.join(
#             folder,
#             "%(id)s.%(ext)s"
#         ),
#
#         "quiet": True,
#         "no_warnings": True,
#
#         "socket_timeout": 120,
#         "retries": 10,
#         "fragment_retries": 10,
#     }
#
#     with yt_dlp.YoutubeDL(options) as ydl:
#
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
# # =========================
# # VIDEO DOWNLOAD
# # =========================
#
# def download_video(update: Update, context: CallbackContext):
#
#     url = update.message.text.strip()
#
#     # Instagram link ekanligini tekshirish
#     if "instagram.com" not in url:
#
#         update.message.reply_text(
#             "❌ Iltimos, Instagram linkini yuboring."
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
#         # Video yuklash
#         file_path, folder = instagram_download(url)
#
#         # Fayl borligini tekshirish
#         if not os.path.exists(file_path):
#
#             loading_message.edit_text(
#                 "❌ Video topilmadi."
#             )
#
#             return
#
#         # Telegramga yuborish
#         with open(file_path, "rb") as video:
#
#             update.message.reply_video(
#                 video=video,
#                 caption="✅ Instagram video yuklandi!"
#             )
#
#         # Yuklanmoqda xabarini o'chirish
#         loading_message.delete()
#
#     except Exception as error:
#
#         print("Xatolik:", error)
#
#         loading_message.edit_text(
#             "❌ Video yuklab bo'lmadi.\n\n"
#             "Instagram linkini tekshirib qayta urinib ko'ring."
#         )
#
#     finally:
#
#         # Vaqtinchalik papkani o'chirish
#         if folder and os.path.exists(folder):
#
#             shutil.rmtree(
#                 folder,
#                 ignore_errors=True
#             )
#
#
# # =========================
# # MAIN
# # =========================
#
# def main():
#
#     updater = Updater(
#         TOKEN,
#         use_context=True
#     )
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
#     # Oddiy text xabarlar
#     dispatcher.add_handler(
#         MessageHandler(
#             Filters.text & ~Filters.command,
#             download_video
#         )
#     )
#
#     print("🤖 Bot ishga tushdi......")
#
#     updater.start_polling()
#
#     updater.idle()
#
#
# # =========================
# # RUN
# # =========================
#
# if __name__ == "__main__":
#     main()
# from telegram import Update,ReplyKeyboardMarkup,ReplyKeyboardRemove
# from telegram.ext import Application, CommandHandler, ContextTypes,filters,MessageHandler
#
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Salom /button burugi orqali tugmalrni korishingiz mumkin!")
# # async def oddiy_xabar(update: Update, context: ContextTypes.DEFAULT_TYPE):
# #     await update.message.reply_text("notori malumot kiritidiz shekilli")
# async def button(update:Update,context:ContextTypes.DEFAULT_TYPE):
#     buttons=[
#         ["loki"],
#         ["thanos"],["baloney"]
#
#     ]
#     markup = ReplyKeyboardMarkup(buttons,one_time_keyboard=False,resize_keyboard=True)
#
#
#
#
#
#
#
#     await update.message.reply_text("tugmalardan birini tanlng",
#                                     reply_markup=markup)
#
# async def bulton(update:Update, context:ContextTypes.DEFAULT_TYPE):
#     text=update.message.text
#     if text=="loki":
#         await update.message.reply_text("ismi:loki\n,"
#                                         "yoshi:15\n"
#                                         ","
#                                         "kuchi:ahmoq")
#     elif text=="thanos":
#         await update.message.reply_text("ismi:thanos,\n"
#                                         "yoshi:150,")
#     elif text=="baloney":
#         await update.message.reply_text("ismi:nomalum,\n"
#                                         "yoshi:,")
#     else:
#         await update.message.reply_text("notugri malumot shekilli")
# async def stop(update:Update, context:ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("tugmani tugatdingiz",
#                                     reply_markup=ReplyKeyboardRemove())
#
#
# app = Application.builder().token("8955884003:AAE-yFRvhIVgdolFzQcW0XsOLsZxlAHIWto").build()
#
# app.add_handler(CommandHandler("start", start))
# app.add_handler(CommandHandler("button", button))
# app.add_handler(
#  MessageHandler(filters.TEXT & ~filters.COMMAND,bulton)
# )
# app.add_handler(CommandHandler("stop", stop))
#
# app.run_polling()



# from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
#
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext
#
#
# async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
#     full_name = update.effective_user.full_name
#     await update.message.reply_text(f"salom {full_name}, botimizga xush kelibsiz /button burugi orqali tugma chiqarishing ,mumkin boladi")
# async def buttons(update: Update, context: CallbackContext):
#     buttons=[
#         ["loki"],["kala"],
#         ["kul"],["kel"]
#     ]
#     marup=ReplyKeyboardMarkup(buttons,one_time_keyboard=False,resize_keyboard=True)
#
#     await update.message.reply_text("tugmalrdan birni tanlang",reply_markup=marup)
#
# async def help(update: Update, context: CallbackContext):
#     text = update.message.text
#     if text=="loki":
#         await update.message.reply_text("ismi: loki\n"
#                                         "yoshi:150")
#     elif text=="kala":
#         await update.message.reply_text("ismi: kala\n")
#     else:
#         await update.message.reply_text("okaaaaaa yannna noturi yozib qoydiz maninimcha")
# async def stop(update: Update, context: CallbackContext):
#     await update.message.reply_text("siz muvaffaqiyatli ravishf]da dasturni toxtattiz",reply_markup=ReplyKeyboardRemove())
#
# lip=Application.builder().token("8955884003:AAF10_H-SLIOdtwJxBEp1pNz60zFrLlyjb4").build()
# lip.add_handler(CommandHandler("start", start))
# lip.add_handler(CommandHandler("buttons", buttons))
# lip.add_handler(CommandHandler("stop", stop))
#
# lip.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,help))
#
#
#
# lip.run_polling()