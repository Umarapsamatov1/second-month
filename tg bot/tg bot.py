# import  os
# import shutil
# import uuid
#
# import yt_dlp
# from dotenv import load_dotenv
#
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, updater
#
# load_dotenv()
#
# TOKEN = os.getenv('BOT_TOKEN')
#
# DOWNLOAD_FOLDER='downloads'
# os.makedirs(DOWNLOAD_FOLDER,exist_ok=True)
#
# def start(update:Update, context:CallbackContext):
#
#     update.message.reply_text("salom  instagram yuklovchi botga xush kelibsiz "
#                               "reel(video) yuklash uchun link yuboring ")
#
#
# def instagram_download(url):
#
#     random_name = str(uuid.uuid4())
#
#     folder=os.path.join(
#         DOWNLOAD_FOLDER,
#         random_name
#     )
#     os.makedirs(folder,exist_ok=True)
#
#
#     options={
#         "format":'best',
#         "outtmpl":os.path.join(
#             folder,
#             "%(id)s.%(ext)s%"
#         ),
#         "quiet":True,
#         "no_warnings":True,
#
#
#     }
#
#     with yt_dlp.YoutubeDL(options) as ydl:
#         info = ydl.extract_info(url,
#                                 download=True)
#
#         file_path=ydl.prepare_filename(info)
#
#     return file_path, folder
#
# def download_video(update:Update, context:CallbackContext):
#     url=update.message.text.strip()
#
#     if "instagram.com" not in url:
#         update.message.reply_text(
#             "instagram linkinin yuboring qandaydur muammo bor"
#         )
#         return
#     loading_message=update.message.reply_text(
#             "video yuklanmoqda"
#         )
#     folder = None
#
#
#
#
#
#
#
#
#     try:
#         file_path, folder=instagram_download(url)
#
#         if not os.path.exists(file_path):
#             loading_message.edit_text(
#                 "video topilmadi"
#             )
#             return
#         with open(file_path, "rb",) as video:
#             update.message.reply_video(
#                 video=video,
#                 caption="instagram video yuklandi"
#             )
#         loading_message.delete()
#
#     except Exception as error:
#         print("xatolik:", error)
#         loading_message.edit_text(
#             "video yuklab bolmadi"
#         )
#
#     finally:
#         if folder and os.path.exists(folder):
#             shutil.rmtree(
#                 folder,
#                 ignore_errors=True
#             )
# def main():
#     updater = Updater(
#         TOKEN,
#         use_context=True
#     )
#
#
#
#     dispatcher = updater.dispatcher
#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command,download_video  ))
#
#     print("bot ishga tushdi......")
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == "__main__":
#     main()
#
#
#
#
#
#
#
# ism=input("enter your name")
# familiyasi=input("enter your familiyasi")
# yosh=int(input("enter your yosh"))
# info=[ism,familiyasi,yosh]
# print(info)





























