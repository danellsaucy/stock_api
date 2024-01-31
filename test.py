from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf

#print(stock_data)


def get_earnings(ticker):
    stock = yf.Ticker()
    stock_data = stock.history(period="max")
    ES = stock.get_earnings_dates()

    earnings_dates = []
    earnings_overall = []
    current_time = pd.to_datetime(datetime.now()).tz_localize('UTC')

    for index, row in ES.iterrows():
        if index < current_time:
            earnings_dates.append(index)
            earnings_overall.append(row['Surprise(%)'])
    print(earnings_dates)
    print(earnings_overall)

    stock_performance = []

    for date in earnings_dates:
        if date.weekday() == 0:
            start_date = date.strftime('%Y-%m-%d')
        else:
            days_until_last_monday = date.weekday()
            start_date = (date - timedelta(days=days_until_last_monday)).strftime('%Y-%m-%d')
        if date.weekday() == 4:
            end_date = date.strftime('%Y-%m-%d')
        else:
            days_until_next_friday = (4 - date.weekday() + 7) % 7
            end_date = (date + timedelta(days=days_until_next_friday)).strftime('%Y-%m-%d')

        try:
            stock_performance.append("{:.2f}".format(stock_data.loc[end_date]["Open"]/stock_data.loc[start_date]["Open"]))
        except:
            stock_performance.append("ERROR")

    print(stock_performance)

def get_options(ticker):
    stock_symbol = 'AAPL'

    # Fetch options data
    stock = yf.Ticker(stock_symbol)
    options_data = stock.options

    current_date = datetime.now()

    for date in options_data:
        # Choose an expiration date from the list
        expiration_date = date  # Replace with the desired date
        days_until_expiration = (datetime.strptime(expiration_date, '%Y-%m-%d') - current_date).days

        if days_until_expiration > 25:
            continue
        # Fetch options data for the chosen expiration date
        options_chain = stock.option_chain(expiration_date)

        # Access call and put options data
        call_options = options_chain.calls
        put_options = options_chain.puts

        print(f'CALLS ({date}): {call_options}')
        print(f'PUTS ({date}): {put_options}')
if __name__ == "__main__":
    get_options('APPL')
# stock_symbol = "MSFT"

# stock_data = yf.download(stock_symbol, start=start_date, end=start_date)

# if not stock_data.empty:
#     start_price = stock_data['Open'][0]
#     print(f"The starting price of {stock_symbol} on {start_date}: {start_price}")
# else:
#     print(f"No data available for {stock_symbol} on {start_date}")

#print(ES)