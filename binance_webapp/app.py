from flask import Flask, render_template, request, flash, redirect, jsonify
import config
from binance.client import Client
from binance.enums import *

app = Flask(__name__)
app.secret_key = b',ajhsfyebfhsbfuyqbghlsbgleqbrg'
client = Client(config.API_KEY, config.API_SECRET)

@app.route('/')
def index():
    title = "CoinView"
    info = client.get_account()
    my_balances = info['balances']
    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']
    return render_template('index.html', title=title, my_balances=my_balances, symbols=symbols)

@app.route('/buy', methods=["POST"])
def buy():
    print(request.form)

    # try:
    #     order = client.create_order(
    #                         symbol='ADA',
    #                         side=SIDE_BUY,
    #                         type=ORDER_TYPE_MARKET,
    #                         quantity=1)
    # except Exception as e:
    #     flash(e.message, "error")

    q = request.form['quantity']
    s = request.form['symbol']
    return 'Buy {quantity} from {symbol}'.format(quantity=q, symbol=s)
    # return redirect('/')

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'

@app.route('/history')
def history():
    candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jul, 2020", "12 Jul, 2020")
    processed_candlesticks = []
    for candle in candles:
        data = { 'time': candle[0]/1000, 'open': candle[1], 'high': candle[2], 'low': candle[3], 'close': candle[4] }
        processed_candlesticks.append(data)
    return jsonify(processed_candlesticks)
