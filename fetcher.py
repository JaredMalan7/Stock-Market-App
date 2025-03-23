import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    # Uses yfinance to retrieve stock data between the start and end dates
    stock = yf.Ticker(ticker)
    df = stock.history(start=start, end=end)
    return df