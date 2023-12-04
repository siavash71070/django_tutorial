import requests
import json
import pyttsx3


class Coindesk:
    def __init__(self):
        self.engine = pyttsx3.init()

    def btc_price(self):
        res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        receive_data = res.text
        data = json.loads(receive_data)
        btc_price = data["bpi"]["USD"]["rate"].replace(",", "")
        price = int(float(btc_price))
        self.engine.say("Bitcoin price is {}".format(price))
        self.engine.runAndWait()
        print(int(float(btc_price)))


if __name__ == "__main__":
    win = Coindesk()
    win.btc_price()
