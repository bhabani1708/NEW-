import requests
import time
import telebot
import os


BOT_TOKEN = "7181559765:AAGAr04ECDvpveY5CaW-n2iHmV4xO1JxPRs"
CHAT_ID = "1727521702"


COINGLASS_API_KEY = os.getenv("5c1ec8ed34f842ea89eb770c44a43a2f")

bot = telebot.TeleBot(BOT_TOKEN)

def get_btc_signal():
    url = "https://open-api.coinglass.com/public/v2/futures/liquidation_chart?symbol=BTC&interval=15min"
    headers = {
        "accept": "application/json",
        "coinglassSecret": COINGLASS_API_KEY
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        if not data or "data" not in data:
            return "⚠️ No signal data."

        latest = data["data"][-1]
        long_liq = latest["longVol"]
        short_liq = latest["shortVol"]

        if long_liq > short_liq:
            direction = "🔻 SHORT"
        elif short_liq > long_liq:
            direction = "🟢 LONG"
        else:
            direction = "🔁 Neutral"

        signal = f"""
🚨 BTC Signal (15min):
Direction: {direction}
🔴 Short Liq: {short_liq:,.2f}
🟢 Long Liq: {long_liq:,.2f}
🎯 Entry: Based on real-time heatmap
TP / SL: Adjust per volatility
        """
        return signal.strip()
    except Exception as e:
        return f"Error: {e}"

def send_signal():
    signal = get_btc_signal()
    bot.send_message(CHAT_ID, signal)

# Keep sending every 15 minutes
while True:
    send_signal()
    time.sleep(900)  # 15 * 60 seconds
