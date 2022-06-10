import requests

url = 'https://api-ssl.bitly.com/v4/user'
headers = {
	"Authorization" : "Bearer 5980aab052614ad9cb069a667062873e38f81eda"
}
response = requests.get(url, headers=headers)
print(response.text)