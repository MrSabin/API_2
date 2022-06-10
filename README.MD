# Script for making short links via Bitly service and monitoring number of clicks

## Installation
1. Download repository
2. Install dependencies by running 
```python
python -m pip install -r requirements.txt
```

## Getting Bitly access token
1. Complete registration on [bitly.com](https://bitly.com)
2. Log in to your account
3. Go to Settings > Developer Settings > API and press `Generate token`

## Running
1. Create .env file in script directory, then put in your Bitly access token, like: 
```python
TOKEN="your_token"
```
2. Run script with parameter `-url "your_url"`
```python
python main.py -url "your_url"
```