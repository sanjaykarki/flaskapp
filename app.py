from flask import Flask, jsonify, json, request
import time
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def btcConverter():

    # current time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

    # Price of 1 BTC in EUR
    coindesk_api = "https://api.coindesk.com/v1/bpi/currentprice.json"
    cdData = requests.get(coindesk_api).json()
    euro = cdData['bpi']['EUR']['rate_float']

    # Price of 1 BTC in CZK
    # forex api for current exchange rate for 1 EUR to CZK
    forex_api = "https://theforexapi.com/api/latest"
    fxData = requests.get(forex_api).json()
    czk = fxData['rates']['CZK']
    czk_btc = round((euro * czk), 4)

    # creating dictionary
    data = {
    "server_time": current_time,
    "EUR": euro,
    "CZK": czk_btc
    }
    return jsonify({'BTC': data})


if __name__ == "__main__":
    app.run(debug=True)