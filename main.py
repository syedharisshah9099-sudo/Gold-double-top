import os
import time
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

SYMBOL = "GC=F"
TIMEFRAME = "1m"
SCAN_INTERVAL = 300
LOOKBACK_CANDLES = 45
MIN_GAP = 5
MAX_GAP = 7
ALERT_PERCENT = 90

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def log(message):
    logging.info(message)


def initialize():
    log("=" * 50)
    log("Gold Double Top Trading Alert System")
    log("System Started")
    log(f"Symbol: {SYMBOL}")
    log(f"Timeframe: {TIMEFRAME}")
    log("=" * 50)


def scan_market():
    log("Checking market...")
    # Yahoo Finance data logic will be added in Part 2
    return None


def detect_double_top(data):
    # Double Top detection will be added in Part 3
    return False


def send_alert():
    # Telegram alert will be added in Part 4
    log("Alert Triggered")


def main():
    initialize()

    while True:
        try:
            market = scan_market()

            if market is not None:
                if detect_double_top(market):
                    send_alert()

            time.sleep(SCAN_INTERVAL)

        except Exception as e:
            logging.exception(e)
            time.sleep(60)


if __name__ == "__main__":
    main()
