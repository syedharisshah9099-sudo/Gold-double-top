from data import get_market_data
from pattern import detect_double_top
from telegram import send_alert

def main():
    print("Gold Double Top Trading Alert System Started...")

    data = get_market_data()

    if data is None:
        print("No market data received.")
        return

    if detect_double_top(data):
        send_alert("🚨 Gold Double Top Alert!\n90% Pattern Completed.")
    else:
        print("No Double Top Found.")

if __name__ == "__main__":
    main()
