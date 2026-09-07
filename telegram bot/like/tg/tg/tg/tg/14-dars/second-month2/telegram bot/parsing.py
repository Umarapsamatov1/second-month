import json
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

def parsing(category):
    info_list = []
    load_dotenv(".env.py")

    HOST = os.getenv("HOST")
    URL = os.getenv("URL")

    HEADERS = {
        "USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
    }
    html=requests.get(URL + category,headers=HEADERS).text
    soul=BeautifulSoup(html,"html.parser")

    card=soul.find_all("div", class_="col-3")
    print(card)
parsing("katalog/smartfony-apple/")