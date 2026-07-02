import datetime as dt

def convert_utc_to_ist(df):
    df["Datetime"] = df["Datetime"].dt.tz_convert("Asia/Kolkata")
    df["Trade_Date"] = df["Datetime"].dt.date
    return df