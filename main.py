# import json
# import requests
# from bs4 import BeautifulSoup
# from dotenv import load_dotenv
# import os
#
#
# def pars_texno(category):
#
#     texno_data = []
#
#     load_dotenv()
#     URL = os.getenv("URL")
#     HOST = os.getenv("HOST")
#     HEADERS = {
#         'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36'
#     }
#
#     html = requests.get(URL + category, headers=HEADERS).text
#
#     soup = BeautifulSoup(html, 'html.parser')
#
#     blocks = soup.find_all('div', class_='col-6')
#     for block in blocks:
#         image_link = block.find("img", class_="img-fluid")
#         if image_link:
#             # Barcha joyda bir xil 'img_tagg' nomidan foydalanamiz
#             img_tagg = image_link.get('src')
#
#             if not img_tagg:
#                 img_tagg = image_link.get('data-fallback')
#
#             print(img_tagg)
#
# pars_texno("product/telefony-i-gadzhety/telefony/smartfony")

# import json
# import requests
# from bs4 import BeautifulSoup
# from dotenv import load_dotenv
# import os
#
#
# def pars_texno(category):
#     texno_data = []
#
#     load_dotenv()
#     URL = os.getenv('URL')
#     HOST = os.getenv('HOST')
#
#     HEADERS = {
#         'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36'
#     }
#
#     html = requests.get(URL + category, headers=HEADERS).text
#     soup = BeautifulSoup(html, 'html.parser')
#
#     blocks = soup.find_all('div', class_='col-3')
#
#     print(blocks)
#
#
# pars_texno('katalog/smartfony-apple/')