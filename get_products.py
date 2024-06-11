import requests
from bs4 import BeautifulSoup
import brand_dictionary as bd
import logging
import random

logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

#Makes request look like its coming from a real user, harder to detect as a bot
user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]

def get_products(brand_map) -> list:
    ctlg = []
    page = 1
    url = brand_map['url']
    
    logging(url)

    if not brand_map['dynamic']:
        while True:
            if page > 1:
                url = f"{url}&page={page}"
            else:
                url = url

            response = requests.get(url, headers={'User-Agent': random.choice(user_agents_list)})
            soup = BeautifulSoup(response.content, 'html.parser')

            items = soup.find_all('div', class_ = brand_map['finder'])
            if not items:
                break

            for item in items:
                # Use keywords to append name, price, and image into items
                name_tag = item.find('div', brand_map['name'])
                name = name_tag.text if name_tag else 'No name found'

                price_tag = item.find('div', brand_map['price'])
                price = price_tag.text if price_tag else 'No price found'

                image_tag = item.find('img', brand_map['image'])
                imageurl = image_tag.get('src') if image_tag else 'No image URL found'

                ctlg.append({'name': name,
                            'price': price,
                            'imageurl': imageurl})
            

            page += 1
    else:
        response = requests.get(url, headers={'User-Agent': random.choice(user_agents_list)})
        soup = BeautifulSoup(response.content, 'html.parser')

        items = soup.find_all('div', class_ = brand_map['finder'])

        for item in items:
            # Use keywords to append name, price, and image into items
            name_tag = item.find('div', brand_map['name'])
            name = name_tag.text if name_tag else 'No name found'

            price_tag = item.find('div', brand_map['price'])
            price = price_tag.text if price_tag else 'No price found'

            image_tag = item.find('img', brand_map['image'])
            imageurl = image_tag.get('src') if image_tag else 'No image URL found'

            ctlg.append({'name': name,
                        'price': price,
                        'imageurl': imageurl})
            
    return ctlg


listt = get_products(bd.parsing_keywords['Nike'])

print(len(listt))




