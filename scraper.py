# Gets current stock price data from google finance
# for all stocks in the ticker.txt file
# Author: Shawn Shaligram

import urllib
from bs4 import BeautifulSoup

tickerFile = open("ticker.txt")
tickerList = tickerFile.read()
tickerArr = tickerList.split("\n")
BASE_URL = "https://www.google.com/finance?q=NASDAQ%3A"

def get_stock_price():
    """
    Scrapes google finance and the ticket symbol
    page and returns stock price for each symbol
    """
    try:
        print "Attempt to gather price data for ticker symbols"
        for ticker in tickerArr:
            try:
                htmlfile = urllib.urlopen(BASE_URL + ticker)
                htmltext = htmlfile.read()

                soup = BeautifulSoup(htmltext, 'html.parser')
                market_data = soup.find('span', attrs={'class' : 'pr'})
                stock_price = market_data.text.strip()
                print ticker,": $",stock_price
            except:
                print("Stock price not found" + ticker)
    except Exception, e:
        print str(e)
        print 'Error occured in returning stock price. Please ensure the ticker symbol is correct'

get_stock_price()