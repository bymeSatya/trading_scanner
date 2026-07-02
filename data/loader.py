import yfinance as yf

def load_market_data(symbols, period, interval):
  ticker = [f"{i}.NS" for i in symbols]
  df_5m = yf.download(tickers=ticker, period=period, interval=interval)
  return df_5m