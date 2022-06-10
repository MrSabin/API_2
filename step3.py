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
	answer = response.json()
	return(answer.get("id"))

token = "5980aab052614ad9cb069a667062873e38f81eda"
url = "https://osu.ppy.sh/users/12782105"

print('Битлинк', shorten_link(token, args.url))