from excp import NoFileFoundException, NoDataAvailableException, ParsingDictionaryError
import pandas as pd

def curr_data_srvc(curr, start_date, end_date):
    try:
        data = pd.read_csv(f"Forex-Data/{curr}.csv")
    except Exception:
        raise NoFileFoundException(curr)

    df = pd.DataFrame(data, columns=['Date', 'Price'])
    df['Date']= pd.to_datetime(df['Date'], format="%b %d, %Y")
    records = df.query('`Date` >= @start_date and `Date` <= @end_date').to_dict('records')
    if not bool(records):
        raise NoDataAvailableException(f"No data for the interval from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")

    try:
        result = []
        for dict_elem in records:
            date = dict_elem["Date"]
            price = dict_elem["Price"]
            date_updated = date.strftime("%Y-%m-%d")
            dict_instance = {"date":date_updated, "value":price}
            result.append(dict_instance)
        result.reverse()

    except Exception:
        raise ParsingDictionaryError(f"Internal Server Error: Can't parse the given dictionary")
        
    return result
    
#MACD 
def macd_service(curr, start_date, end_date):
    data = curr_data_srvc(curr, start_date, end_date)
    prices = list(map(lambda x: x['value'], data))
    prices = pd.DataFrame(prices)
    exp1 = prices.ewm(span=12, adjust=False).mean()
    exp2 = prices.ewm(span=26, adjust=False).mean()
    macd = pd.DataFrame(exp1 - exp2)
    return list(map(lambda x:x[0], macd.to_dict('records')))


