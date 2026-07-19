from scanner import get_gold_data
from pattern import detect_double_top
from telegram import send_alert
from state import load_state, save_state


def main():

    print("========================================")
    print(" Gold Double Top Trading Alert System")
    print("========================================")

    state = load_state()

    data = get_gold_data()

    if data is None:
        print("No market data received.")
        return

    signal = detect_double_top(data)

    if signal:

        if not state.get("alert_sent", False):

            send_alert(
                "🚨 GOLD DOUBLE TOP DETECTED\n\n"
                "Pattern Completion: 90%+\n"
                "Timeframe: M1\n"
                "Symbol: GC=F"
            )

            state["alert_sent"] = True
            save_state(state)

            print("Telegram Alert Sent")

        else:
            print("Alert already sent.")

    else:

        state["alert_sent"] = False
        save_state(state)

        print("No Double Top Pattern")


if __name__ == "__main__":
    main()
