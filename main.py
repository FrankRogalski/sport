import requests
from concurrent.futures import ThreadPoolExecutor, wait
from argparse import ArgumentParser

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

def standard():
    while True:
        try:
            while True:
                requests.post('https://www.netto-online.de/vereinsspende/wp-admin/admin-ajax.php', headers=headers, data=data)
        except:
            pass

def threaded(threads):
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(standard) for _ in range(threads)]
        wait(futures)

def main():
    parser = ArgumentParser('Parser for the Posthausen race')
    parser.add_argument('-t', nargs='?', help='run in threaded mode and specify number of threads', type=int)
    args = parser.parse_args()
    if args.t:
        threaded(args.t)
    else:
        standard()

if __name__ == '__main__':
    main()