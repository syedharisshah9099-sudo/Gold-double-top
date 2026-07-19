import pandas as pd

def detect_double_top(data):
    if data is None:
        return False

    if len(data) < 45:
        return False

    highs = data["High"]

    first_top = highs.idxmax()
    first_price = highs.max()

    after = highs.loc[first_top:]

    if len(after) < 5:
        return False

    second_price = after.max()

    progress = (second_price / first_price) * 100

    if progress >= 90:
        return True

    return False
