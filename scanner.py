import yfinance as yf

def get_gold_data():
    data = yf.download(
        "GC=F",
        period="1d",
        interval="1m",
        progress=False
    )

    if data.empty:
        return None

    return data.tail(45)
