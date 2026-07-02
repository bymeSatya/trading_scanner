from config import *
from datetime import datetime
from pathlib import Path

def ensure_dir(path):
  dir_path = Path(path)
  dir_path.mkdir(parents=True, exist_ok=True)

def save_market_data(df):
  symbol_list = df["Symbol"].unique().tolist()
  for symbol in symbol_list:
    symbol_df = df[df["Symbol"]==symbol]
    trade_dates = symbol_df["Trade_Date"].unique()
    for trade_date in trade_dates:
      day_df = symbol_df[symbol_df["Trade_date"]==trade_date]
      store_path = build_storage_path(symbol,INTERVAL,trade_date)
  return store_path

def read_market_data(symbol, interval, start_date=None, end_date=None):
  df = None
  return df

def get_latest_candle(symbol, interval):
  df = None
  return df

def market_data_exists(symbol, interval):
  df = False
  return df

def validate_market_data(symbol, interval):
  return True

def build_storage_path(symbol, interval, trade_date):
    year = trade_date.strftime("%Y")
    month = trade_date.strftime("%m")
    file_name = trade_date.strftime("%Y_%m_%d.parquet")

    store_path = (
        Path(MARKET_DATA_PATH)
        / symbol
        / interval
        / year
        / month
        / file_name
    )

    #store_path.parent.mkdir(parents=True, exist_ok=True)

    return str(store_path)