from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='YH0Q5TEXOFKO0Y7U')

# Get json object with the intraday data and another with  the call's metadata
def getStockData(stock):
    data, meta_data = ts.get_intraday(stock)
    print('Requesting data for ', stock, ': ')

#TODO create a function that will use ts.get_daily to return Daily information

command = '!stock MSFT'

list_string = command.split(' ')
command = list_string[0]
stock = list_string[1]

print('Command: ', command)
print('Stock: ', stock)


#TODO Add support that when using the command !stock_daily it will run your Daily information function
if command == '!stock':
    getStockData(stock)
else:
    print("Not Supported")
