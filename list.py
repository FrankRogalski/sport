import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, wait

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.7,de;q=0.3',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://www.netto-online.de/vereinsspende/projekte.html?postcode=28870&radius=3000',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'TE': 'trailers',
}

vereine = []
def get_page(i):
    params = (
        ('type', 'load_more'),
        ('my_paged', str(i)),
        ('postcode', '28870'),
        ('radius', '30000'),
        ('load_more_text', 'Mehr anzeigen'),
        ('ajax', '1'),
    )

    response = requests.get('https://www.netto-online.de/vereinsspende/', headers=headers, params=params)#, cookies=cookies)

    bs = BeautifulSoup(response.content, features='html.parser')
    for card in bs.find_all('div', {'class': 'card'}):
        title = card.find_next('h3', {'class': 'card-title'}).text
        location = card.find_next('span', {'class': 'card-location'}).text
        likes = int(card.find_next('span', {'class': 'count-box'}).text[1:].replace(".", ""))
        vereine.append((title, likes, location))


with ThreadPoolExecutor(max_workers=100) as executor:
    futures = [executor.submit(get_page, i) for i in range(160)]
    wait(futures)
vereine = sorted(set(vereine), key=lambda x: x[1], reverse=True)
with open('/Users/frankrogalski/Privat/Python/2021-08-09 sport/jo.txt', 'w') as file:
    for verein in vereine:
        file.write(str(verein) + '\n')

print(len(vereine))