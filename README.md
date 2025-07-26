# BTC Signal Telegram Bot (CoinGlass Based)

This bot sends 15-minute BTC liquidation data signals (Long/Short with TP/SL hints) using CoinGlass API.

## Setup
1. Set `BOT_TOKEN`, `CHAT_ID`, and `COINGLASS_API_KEY` in environment variables or in `main.py`.
2. Deploy to Render with Python 3.
3. Logs will show if API is working and bot sends messages.
