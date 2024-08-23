import requests
import time

class Webull:
    def __init__(self, ticker=None):
        self.ticker = ticker
            
    def getTickerId(self, ticker=None):
        url = f'https://quotes-gw.webullfintech.com/api/search/pc/tickers?keyword={ticker}&pageIndex=1&pageSize=1'
        response = requests.get(url=url).json()
        data = response['data']
        return data[0]['tickerId']

    def getStockData(self, ticker=None):
        tickerId = self.getTickerId(ticker)
        url = f'https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={tickerId}&includeSecu=1&delay=0&more=1'
        response = requests.get(url=url).json()
        
        # extracting useful data
        volume = response[0]['volume']
        fiftyTwoWkHigh = response[0]['fiftyTwoWkHigh']
        fiftyTwoWkLow = response[0]['fiftyTwoWkLow']
        open = response[0]['open']
        high = response[0]['high']
        low = response[0]['low']
        close = response[0]['close']

        # creating dictionary to store this data, allowing for easy access
        data = {'ticker': ticker,
                'open': open,
                'close': close,
                'high': high,
                'low': low,
                'volume': volume,
                '52 Wk High': fiftyTwoWkHigh,
                '52 Wk Low': fiftyTwoWkLow}

        return data
    
    def getLivePrice(self, ticker=None, frequency=5):
        tickerId = self.getTickerId(ticker)

        while True:
            url = f'https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={tickerId}&includeSecu=1&delay=0&more=1'
            response = requests.get(url=url).json()
            close = response[0]['close']
            print(f'{ticker} current price = {close}')
            time.sleep(frequency)