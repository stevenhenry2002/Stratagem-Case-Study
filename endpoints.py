from getting_live_data import Webull
import requests

# Getting the ticker ID
webullData = Webull()
tickerId = webullData.getTickerId('MSFT')

# Useful endpoints from Webull to get useful data
cashflow = f'https://quotes-gw.webullfintech.com/api/information/financial/cashflow?tickerId={tickerId}&type=101&fiscalPeriod=0&limit=10'
balanceSheet = f'https://quotes-gw.webullfintech.com/api/information/financial/balancesheet?tickerId={tickerId}&type=101&fiscalPeriod=0&limit=10'
incomeStatement = f'https://quotes-gw.webullfintech.com/api/information/financial/incomestatement?tickerId={tickerId}&type=101&fiscalPeriod=0&limit=10'
forecast = f'https://quotes-gw.webullfintech.com/api/information/financial/forecast?tickerId={tickerId}&statementType=1'
analystRatings = f'https://quotes-gw.webullfintech.com/api/information/securities/analysis?tickerId={tickerId}'
priceTarget = f' https://quotes-gw.webullfintech.com/api/market/stock/recommendation?tickerId={tickerId}'

def getDataFromEndpoint(endpoint):
    response = requests.get(url=endpoint).json()
    return response