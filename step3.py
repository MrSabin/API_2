import argparse

import requests

parser = argparse.ArgumentParser()
parser.add_argument('-url', help = 'URL для сокращения')
args = parser.parse_args()

def shorten_link(token, url):
	bitly_url = "https://api-ssl.bitly.com/v4/bitlinks"

	headers = {"Authorization" : f"Bearer {token}"}
	body = {"long_url" : f"{url}"}

	response = requests.post(bitly_url, headers=headers, json=body)
	response.raise_for_status()
	answer = response.json()
	return answer.get("id")

def count_clicks(token, link):
	bitly_url = f"https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary"

	headers = {"Authorization" : f"Bearer {token}"}
	params = {"units" : "-1"}

	response = requests.get(bitly_url, headers=headers, params=params)
	response.raise_for_status()
	answer = response.json()
	return answer.get("total_clicks")

token = "5980aab052614ad9cb069a667062873e38f81eda"

try:
	bitlink = shorten_link(token, args.url)
	print('Битлинк', bitlink)
	print('Количество кликов:', count_clicks(token, bitlink))
except requests.exceptions.HTTPError:
	print("Задана неверная ссылка")