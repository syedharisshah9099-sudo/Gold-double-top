import yfinance as yf

def get_market_data():
    data = yf.download(
        tickers="GC=F",
        period="1d",
        interval="1m",
        progress=False,
        auto_adjust=True
    )

    if data.empty:
        return None

    return data.tail(45)
    
