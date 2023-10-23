import requests
from datetime import datetime, timedelta

api_key = "ulQSqrmpqo2w1CpABI7W9ZQ4xkO3D7sc"

codes = {
    'AAPL': 'Apple',
    'TSLA': 'Tesla'
}


def request(stock_id, start_date, end_date):
    url = f"https://api.polygon.io/v2/aggs/ticker/{stock_id}/range/1/day/{start_date}/{end_date}?apiKey={api_key}"
    return formatStock(requests.get(url).json(), start_date, end_date)


def formatStock(response, start_date, end_date):
    date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

    increment = 0
    data = {'stock_code': response['ticker']}
    while date < end_date:
        if date.weekday() > 4:
            date += timedelta(days=1)
            continue
        temp = {
            'price': response["results"][increment]["c"]
        }
        date += timedelta(days=1)
        increment += 1
        data[date.strftime("%Y-%m-%d")] = temp
    return data


if __name__ == '__main__':
    formatted = request('AAPL', '2023-10-01', '2023-10-21')
    print(formatted)
