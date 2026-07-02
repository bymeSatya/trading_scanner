def normalize_market_data(df):
    #print("normalize_market_data() called")
    df = df.stack()
    df = df.reset_index()
    df["Ticker"] = df["Ticker"].str.replace(".NS", "", regex=False)
    df = df.rename(columns={"Ticker": "Symbol"})
    column_order = ["Symbol", "Datetime", "Open", "High", "Low", "Close", "Volume"]
    df = df[column_order]
    df.columns.name = None
    return df