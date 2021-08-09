import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.7,de;q=0.3',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.netto-online.de',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.netto-online.de/vereinsspende/vereinsspende.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'TE': 'trailers',
}

data = {
    'action': 'wp_ulike_process',
    'id': '923',
    'nonce': '1c9db1577e',
    'type': 'post',
    'template': 'wpulike-default',
    'displayLikers': '0',
    'likersTemplate': 'popover'
}

i = 0
while True:
    requests.post('https://www.netto-online.de/vereinsspende/wp-admin/admin-ajax.php', headers=headers, data=data)
    i += 1
    if i % 100 == 0:
        print(f'{i} requests done')
