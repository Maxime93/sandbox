# BINANCE WebApp
From: https://www.youtube.com/watch?v=rvhnz1yBHgQ

## Flask env variables
$ export FLASK_APP=main.py
$ export FLASK_ENV=development
$ flask run

## Data
wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m | tee dataset.txt
{"e":"kline","E":1594775215998,"s":"BTCUSDT","k":{"t":1594775100000,"T":1594775399999,"s":"BTCUSDT","i":"5m","f":355635648,"L":355636415,"o":"9264.07000000","c":"9261.54000000","h":"9264.14000000","l":"9259.05000000","v":"31.14132100","n":768,"x":false,"q":"288417.21653402","V":"14.84083100","Q":"137451.65997958","B":"0"}}

{"e":"kline","E":1594775478076,"s":"BTCUSDT","k":{"t":1594775400000,"T":1594775699999,"s":"BTCUSDT","i":"5m","f":355637407,"L":355637688,"o":"9256.72000000","c":"9256.61000000","h":"9257.83000000","l":"9256.60000000","v":"9.08364000","n":282,"x":false,"q":"84085.72593882","V":"3.60296000","Q":"33351.67608572","B":"0"}}

## WebApp