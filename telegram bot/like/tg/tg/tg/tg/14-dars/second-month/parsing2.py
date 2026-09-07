import json
import requests
from bs4 import BeautifulSoup
from dotenv import find_dotenv, load_dotenv
import os

def parsing(item):

    info=[]

    load_dotenv()
    QUOTES_HOST=os.getenv("QUOTES_HOST")
    QUOTES_URL=os.getenv("QUOTES_URL")

    HEADERS={
        "USER-AGENT":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36'
    }
    html=requests.get(item,headers=HEADERS).text
    soup=BeautifulSoup(html,"html.parser")

    blocks=soup.find_all('div', class_='quote')
    for block in blocks:
       quote=block.find('span', class_='text').text.strip()
       author=block.find('small', class_='author').text.strip()
       tags=[tag.text.strip()for tag in block.find_all('a',class_='tag')]
       author_link_elem=block.find('a', string ='(about)')
       author_link ="https://quotes.toscrape.com" + author_link_elem['href']if author_link_elem else None
       source_url=item
       info.append({
           "quote":quote,
           "author":author,
           "tags":tags,
           "author_link":author_link,
           "source_url":source_url
       })
    with open("malumot.json","w", encoding="utf-8") as file:
        json.dump(info,file,ensure_ascii=False,indent=4)
    print(info)
parsing("https://quotes.toscrape.com")
