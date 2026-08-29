# import os
# import shutil
# import uuid
#
# import yt_dlp
# from dotenv import load_dotenv
#
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
#
# load_dotenv()
#
# TOKEN = os.getenv('BOT_TOKEN')
#
# DOWNLOAD_FOLDER = 'downloads'
# os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
#
#
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "👋 Salom\n\n"
#         "Instagramdan video yuklab beruvchi botman.\n\n"
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
#     file_path = os.path.join(folder, "video.mp4")
#
#     options = {
#         "format": "bestvideo+bestaudio/best",
#         "outtmpl": file_path,
#         "quiet": True,
#         "no_warnings": True,
#         "http_headers": {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
#             "Referer": "https://www.instagram.com/",
#         }
#     }
#
#     with yt_dlp.YoutubeDL(options) as ydl:
#         ydl.download([url])
#
#     return file_path, folder
#
#
# async def download_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     url = update.message.text.strip()
#
#     if "instagram.com" not in url:
#         await update.message.reply_text(
#             "Instagram link yuboring, qandaydir muammo bor ❌"
#         )
#         return
#
#     loading_message = await update.message.reply_text(
#         "⏳ Video yuklanmoqda..."
#     )
#
#     folder = None
#
#     try:
#         file_path, folder = await context.application.loop.run_in_executor(
#             None, instagram_download, url
#         )
#
#         if not os.path.exists(file_path):
#             await loading_message.edit_text(
#                 "❌ Video topilmadi."
#             )
#             return
#
#         with open(file_path, "rb") as video:
#             await update.message.reply_video(
#                 video=video,
#                 caption="Instagram video yuklandi ✅"
#             )
#
#         await loading_message.delete()
#
#     except Exception as error:
#         print("Xatolik:", error)
#         await loading_message.edit_text(
#             "Video yuklab bo'lmadi ❌"
#         )
#
#     finally:
#         if folder and os.path.exists(folder):
#             shutil.rmtree(
#                 folder,
#                 ignore_errors=True
#             )
#
#
# def main():
#     app = ApplicationBuilder().token(TOKEN).build()
#
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))
#
#     print("Bot ishga tushdi...")
#
#     app.run_polling()
#
#
# if __name__ == "__main__":
#     main()