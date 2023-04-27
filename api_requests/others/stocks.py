import math
from datetime import datetime, timedelta

import requests
from twilio.rest import Client

from api_requests.others.data import *


def get_date(days):
    date = datetime.now() - timedelta(days)
    return date.strftime("%Y-%m-%d")


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def get_top_3_news():
    news_endpoint = "https://newsapi.org/v2/everything"
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    response = requests.get(url=news_endpoint, params=news_parameters)
    articles = response.json()["articles"][:3]
    news = {}
    for article in articles:
        news[article['title']] = article['description']
    return news


def get_stock_price(day):
    alphavantage_end_point = "https://www.alphavantage.co/query"
    stock_parameters = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "apikey": ALPHAVALTAGE_API_KEY,
    }
    response = requests.get(url=alphavantage_end_point, params=stock_parameters)
    response_json = response.json()
    all_days_data = response_json["Time Series (Daily)"]
    particular_day_data = all_days_data[get_date(day)]
    particular_day_close = particular_day_data["4. close"]
    return float(particular_day_close)


def change_more_than_5():
    close_21 = get_stock_price(4)
    close_20 = get_stock_price(5)
    change = (close_21 - close_20) / close_20 * 100
    change = math.floor(change)
    if change > 0:
        return f"🔺{change}%"
    elif change < 0:
        return f"🔻{change}%"


def send_msg():
    change = change_more_than_5()
    news = get_top_3_news()
    account_sid = TWILIO_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    for key, value in news.items():
        message = client.messages.create(
            body=f"{STOCK}: {change}\nHeadline: {key}\nBrief: {value}",
            from_=TWILIO_FROM_PHONE_NUMBER,
            to=MY_PHONE_NUMBER
        )
        print(message.status)


if __name__ == '__main__':
    send_msg()
