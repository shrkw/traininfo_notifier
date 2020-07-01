import json
from typing import Dict, List

import requests


class YahooForecastApi:
    path = "tmp/rain_state.txt"

    def __init__(self, location: str, appid: str):
        # Longitude latitude
        self.location = location
        self.appid = appid

    def get_forecast(self) -> List[Dict]:
        url = "https://map.yahooapis.jp/weather/V1/place"
        payload = {
            "coordinates": self.location,
            "appid": self.appid,
            "output": "json",
            "interval": "5",
        }
        r = requests.get(url, params=payload)
        res = json.loads(r.text)
        forecasts = res["Feature"][0]["Property"]["WeatherList"]["Weather"]
        return forecasts

    def get_previous_result(self) -> bool:
        try:
            with open(YahooForecastApi.path) as f:
                line = f.read()
                if line == "True":
                    return True
        except FileNotFoundError:
            print("File not found.")
        return False

    def save_result(self, result: bool) -> None:
        with open(YahooForecastApi.path, "w") as f:
            f.write(str(result))

    def parse(self, forecasts: List[Dict]):
        rainy_forecast = False
        for x in forecasts:
            if x["Rainfall"] > 0:
                rainy_forecast = True

        if not rainy_forecast:
            # 雨が予測されていないなら終了
            print("not rainy forecast")
            self.save_result(False)
            return None

        previousResult = self.get_previous_result()
        self.save_result(True)

        print(f"previous: {previousResult}, current: {rainy_forecast}")
        if (not previousResult) and rainy_forecast:
            # 前回が雨予報でなく、今回のが雨予報なら通知する
            return "ヤフーの気象情報によると、雨雲が近づいており、１時間以内に雨が予測されています。"
        else:
            return None

    def run(self):
        forecasts = self.get_forecast()
        return self.parse(forecasts)
