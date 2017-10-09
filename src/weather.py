# -*- coding: utf-8 -*-
import json

from datetime import datetime

import requests

from src.translation import HindiEnglish


class WeatherYahoo:

    latitude = ""
    longitude = ""

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_json_weather_three_days(self):


        req = requests.get("http://api.openweathermap.org/data/2.5/forecast/daily?lat="+self.latitude+"&lon="+self.longitude+"&cnt=3&mode=json&units=metric&appid=15d62eede0fc0659129e2956202bfc48")
        data = json.loads(req.text)

        forecast_data = {"ty":"we3", "data":[]}

        for forecast in data["list"]:

            date_epoch = forecast["dt"]
            day = (datetime.fromtimestamp(date_epoch).strftime("%A")+"")[:2]
            date = (datetime.fromtimestamp(date_epoch).strftime('%Y-%m-%d %H:%M:%S.%f')+"")[8:10]
            month = (datetime.fromtimestamp(date_epoch).strftime('%Y-%m-%d %H:%M:%S.%f') + "")[5:7]

            temp = forecast["temp"]
            weather = forecast["weather"][0]
            wind_speed = forecast["speed"]
            deg_wind = forecast["deg"]

            trans_desc = HindiEnglish()
            desc_hindi = trans_desc.eng_to_hindi(weather["description"])

            forecast_data["data"].append({"ty":"we3", "da": day, "dt":date, "m": month, "h": temp["max"], "l": temp["min"], "t":desc_hindi, "ic": weather["icon"], "ws": wind_speed, "wd":deg_wind})

            print forecast_data



        return json.dumps(forecast_data)

    def get_json_weather_one_day(self):

        req = requests.get("http://api.openweathermap.org/data/2.5/forecast/daily?lat="+self.latitude+"&lon="+self.longitude+"&cnt=1&mode=json&units=metric&appid=15d62eede0fc0659129e2956202bfc48")
        data = json.loads(req.text)


        forecast_data = {}

        for forecast in data["list"]:

            date_epoch = forecast["dt"]
            day = (datetime.fromtimestamp(date_epoch).strftime("%A")+"")
            date = (datetime.fromtimestamp(date_epoch).strftime('%Y-%m-%d %H:%M:%S.%f')+"")[8:10]
            month = (datetime.fromtimestamp(date_epoch).strftime('%Y-%m-%d %H:%M:%S.%f')+"")[5:7]

            temp = forecast["temp"]
            weather = forecast["weather"][0]
            wind_speed = forecast["speed"]
            deg_wind = forecast["deg"]

            trans_desc = HindiEnglish()
            desc_hindi = trans_desc.eng_to_hindi(weather["description"])

            forecast_data = {"ty":"we1","da": day, "dt":date, "m": month, "h": temp["max"], "l": temp["min"], "t":desc_hindi, "ic": weather["icon"], "ws": wind_speed, "wd":deg_wind}

            print forecast_data


        return json.dumps(forecast_data)

    def get_json_weather_specific_day(self, day_count):

        req = requests.get("http://api.openweathermap.org/data/2.5/forecast/daily?lat="+self.latitude+"&lon="+self.longitude+"&cnt=4&mode=json&units=metric&appid=15d62eede0fc0659129e2956202bfc48")
        data = json.loads(req.text)


        forecast_data = {}

        count = 0

        for forecast in data["list"]:

            if count == day_count:

                date_epoch = forecast["dt"]
                day = (datetime.fromtimestamp(date_epoch).strftime("%A")+"")
                date = (datetime.fromtimestamp(date_epoch).strftime('%Y-%m-%d %H:%M:%S.%f')+"")[8:10]
                month = (datetime.fromtimestamp(date_epoch).strftime('%Y-%m-%d %H:%M:%S.%f')+"")[5:7]

                temp = forecast["temp"]
                weather = forecast["weather"][0]
                wind_speed = forecast["speed"]
                deg_wind = forecast["deg"]

                trans_desc = HindiEnglish()
                desc_hindi = trans_desc.eng_to_hindi(weather["description"])

                forecast_data = {"ty":"we1", "da": day, "dt":date, "m": month, "h": temp["max"], "l": temp["min"], "t":desc_hindi, "ic": weather["icon"], "ws": wind_speed, "wd":deg_wind}

                print forecast_data
                print ":::"+str(count)+":::"

                break

            else:
                count += 1



        return json.dumps(forecast_data)




