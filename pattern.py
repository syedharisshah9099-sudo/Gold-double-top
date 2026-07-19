import pandas as pd

MIN_GAP = 5
MAX_GAP = 7
MAX_CANDLES = 45
TOP_TOLERANCE = 0.003
ALERT_LEVEL = 0.90


def detect_double_top(data):

    if data is None:
        return False

    if len(data) < MAX_CANDLES:
        return False

    highs = list(data["High"])

    first_index = highs.index(max(highs[:20]))
    first_top = highs[first_index]

    start = first_index + MIN_GAP
    end = min(first_index + MAX_CANDLES, len(highs))

    if start >= end:
        return False

    highest = max(highs[start:end])
    second_index = highs.index(highest)

    if second_index - first_index < MIN_GAP:
        return False

    if second_index - first_index > MAX_CANDLES:
        return False

    progress = highest / first_top

    if progress >= ALERT_LEVEL:

        if abs(highest - first_top) / first_top <= TOP_TOLERANCE:
            return True

    return False
