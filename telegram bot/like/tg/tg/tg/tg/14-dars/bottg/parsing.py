import os
import requests
import soup
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

print(soup.prettify()[:2000])
def pars_texno(category):
    texno_data = []

    URL = os.getenv("URL") or "https://asaxiy.uz/"
    HOST = os.getenv("HOST") or "https://asaxiy.uz"

    HEADERS = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    request_url = f"{URL.rstrip('/')}/{str(category).lstrip('/')}"
    response = requests.get(request_url, headers=HEADERS)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, features='html.parser')

    # Mahsulot kartochkalarini qidirish
    blocks = soup.select('div.product__item') or soup.select('div.col-6')

    for block in blocks[:10]:
        # 1. Rasm
        img_tag = block.select_one('img.img-fluid') or block.select_one('img')
        images = None
        if img_tag:
            images = img_tag.get('data-src') or img_tag.get('src')

        # 2. Nom
        title_tag = block.select_one('span.productitemtitle') or block.select_one('h5') or block.select_one(
            'a.productitemtitle')
        title = title_tag.get_text(strip=True) if title_tag else "Noma'lum"

        # 3. Narx
        price_tag = block.select_one('span.productitemprice') or block.select_one('div.productitemprice')
        price = price_tag.get_text(strip=True) if price_tag else "Ko'rsatilmagan"

        # 4. Muddatli to'lov
        credit_tag = block.select_one('div.installment-price') or block.select_one('span.installment-price')
        credit_price = credit_tag.get_text(strip=True) if credit_tag else "Mavjud emas"

        # 5. Havola (Link)
        a_tag = block.select_one('a[href*="/product/"]') or block.select_one('a')
        if a_tag and a_tag.get('href'):
            href = a_tag.get('href')
            link = href if href.startswith('http') else str(HOST).rstrip('/') + '/' + href.lstrip('/')
        else:
            link = str(HOST)

        texno_data.append({
            'images': images,
            'title': title,
            'credit_price': credit_price,
            'price': price,
            'link': link
        })

    return texno_data