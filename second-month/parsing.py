import json
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv


def parse(category):
    load_dotenv()

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    html = requests.get(category, headers=header).text
    soup = BeautifulSoup(html, 'html.parser')

    blocks = soup.find_all('div', class_='thumbnail')

    products = []

    for block in blocks:
        title_elem = block.find('a', class_='title')
        title = title_elem.get('title') or title_elem.text.strip()

        price = block.find('h4', class_='price').text.strip()

        description = block.find('p', class_='description').text.strip()

        image = "https://webscraper.io" + block.find('img')['src']

        product_link = "https://webscraper.io" + title_elem['href']

        products.append({
            "title": title,
            "price": price,
            "description": description,
            "image": image,
            "product_link": product_link
        })

    print(f"Jami topildi: {len(products)} ta mahsulot\n")
    for item in products:
        print(item)

    with open("malumot.json", "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4, ensure_ascii=False)


parse("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")