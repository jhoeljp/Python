STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
#DEPENDECIES
import requests
import datetime as dt
from API_KEYS import STOCK_API_KEY, NEWS_API_KEY

def price_changed():
    ## STOCK PRICE API -> https://www.alphavantage.co
    # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    # STOCK_API_KEY = "QF8ZFZVY1X6I5XQL"

    #Make request for stock information
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_API_KEY}'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    #Access stock info by Date
    data = data['Time Series (Daily)']

    #Get yesterday and the day before yesterday price
    today = dt.datetime.now()
    yesterdays_date = today - dt.timedelta(days=1)
    before_yesterday_date = yesterdays_date - dt.timedelta(days=1)
    #chop time off the dates 
    yesterdays_date = str(yesterdays_date).split(" ")[0]
    before_yesterday_date = str(before_yesterday_date).split(" ")[0]

    #get prices
    price_2days_ago = float(data[before_yesterday_date]['4. close'])
    price_1days_ago = float(data[yesterdays_date]['4. close'])
    # print(f"price_2days_ago: {price_2days_ago} & price_1days_ago: {price_1days_ago}")

    #Calculate percentage price difference 
    increase = price_1days_ago - price_2days_ago
    increase_percent = increase / price_2days_ago* 100
    # print(f"increase percent: {increase_percent}")

    #Determine if percentage change is significant (increased/decreased by 5%?)
    percent = abs(increase_percent)
    percent_str = "%.2f"%(percent)
    delta = ""
    if percent >=5:
        if increase > 0:
            delta = f"{STOCK}: 🔺{percent_str}%"
        else: 
            delta = f"{STOCK}: 🔻{percent_str}%"
    return delta


def get_news():
    ## NEWS API ->  https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

    # Make json request for news of the company
    url = f"https://newsapi.org/v2/top-headlines?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    # Get list of articles 
    articles_list = response.json()['articles']
    # News list is not empty 
    message = ""
    if articles_list:
        # Obtain headline and brief description for TOP 3 articles on COMPANY_NAME
        for article in articles_list[:4]:
            headline = article['title']
            brief = article['description']
            news_url = article['url']
            # print(f"Headline: {headline}\n\nBrief: {brief}\n\nURL: {news_url}")
            message = f"Headline: {headline}\n\nBrief: {brief}\n\nURL: {news_url}"
    return message

def send_email_update(price,msg):
    print(price)
    print(msg)

#START ---------------------------------
#If the stock price change significantly
#lets get some News 
price_chage = price_changed()
if price_chage:
    msg = get_news()
    #if there is news on the company send email update to user
    if msg: send_email_update(price_chage,msg)
    else: print("No News to report at the moment.")
else:
    print("No Significant price change Today! ")