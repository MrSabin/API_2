import argparse
import os
import urllib.parse

import requests
from dotenv import load_dotenv


def is_bitlink(token, url):
    parsed = urllib.parse.urlparse(url)
    url = f"{parsed.netloc}{parsed.path}"
    bitly_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(bitly_url, headers=headers)
    return response.ok


def shorten_link(token, url):
    bitly_url = "https://api-ssl.bitly.com/v4/bitlinks"
    headers = {"Authorization": f"Bearer {token}"}
    body = {"long_url": f"{url}"}
    response = requests.post(bitly_url, headers=headers, json=body)
    response.raise_for_status()
    answer = response.json()
    return answer.get("id")


def count_clicks(token, url):
    parsed = urllib.parse.urlparse(url)
    url = f"{parsed.netloc}{parsed.path}"
    bitly_url = f"https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"units": "-1"}
    response = requests.get(bitly_url, headers=headers, params=params)
    response.raise_for_status()
    answer = response.json()
    return answer.get("total_clicks")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-url', help='URL для сокращения')
    args = parser.parse_args()
    load_dotenv()
    token = os.environ["BITLY_TOKEN"]
    try:
        if is_bitlink(token, args.url):
            print('Количество кликов:', count_clicks(token, args.url))
        else:
            print('Битлинк', shorten_link(token, args.url))
    except requests.exceptions.HTTPError:
        print("Задана неверная ссылка")


if __name__ == '__main__':
    main()
