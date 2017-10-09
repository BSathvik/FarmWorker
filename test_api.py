# -*- coding: utf-8 -*-
import base64
import json
import os

import requests
from flask import Flask
from flask import request

from src.conversation import FarmerConversation
from src.integrate_api import Integrate_API
from src.integrate_sms import Integrate_SMS
from src.maps import GoogleMaps
from src.translation import HindiEnglish
from src.weather import WeatherYahoo

app = Flask(__name__)
app.debug = True


@app.route('/')
def Welcome():
    return app.send_static_file('index.html')


@app.route('/sms_request', methods=['POST'])
def sms_request():

    integrate = Integrate_API(request.form["text"], request.form["number"])
    return integrate.start()


@app.route('/sms_request_callback', methods=['POST'])
def sms_request_call_back():

    integrate = Integrate_SMS(request.form["comments"], request.form["sender"])

    return "I guess it works"+ integrate.start()


@app.route('/sms', methods=['POST'])
def sms():
    req = requests.post("https://api.textlocal.in/send", data={"username": "sathvikbiradavolu@gmail.com",
                                                               "hash": "54433e2d94aa89ff1da199d76bab4fd725412245",
                                                               "sender": "TXTLCL",
                                                               "message": "\"[]<> - this is just testing stuff - the text is::   " +
                                                                          request.form["comments"],
                                                               "numbers": request.form["sender"] + "",
                                                               "test": "false",
                                                               "unicode": "true"})

    return "Shit is here:" + req.text + "   :::: " + request.form["sender"] + " ::: " + request.form["comments"]


@app.route('/weather_three_days', methods=['POST'])
def get_weather_three_days():
    longitude = request.form["long"]
    lat = request.form["lat"]

    weather = WeatherYahoo(lat, longitude)

    return weather.get_json_weather_three_days()


@app.route('/weather_one_day', methods=['POST'])
def get_weather_one_day():
    longitude = request.form["long"]
    lat = request.form["lat"]

    weather = WeatherYahoo(lat, longitude)

    return (weather.get_json_weather_one_day()+"").replace("we1", "pwe1")


@app.route('/hindi_to_eng', methods=['POST'])
def hindi_to_eng():
    translation = HindiEnglish()
    return translation.hindi_to_eng(request.form["hindi_text"])


@app.route('/eng_to_hindi', methods=['POST'])
def eng_to_hindi():
    translation = HindiEnglish()
    return translation.eng_to_hindi(request.form["eng_text"])


@app.route('/maps_distance_time', methods=['POST'])
def maps_dist_time():
    maps = GoogleMaps()
    return maps.distance_json(request.form["lat"], request.form["long"], request.form["dest"])


@app.route('/maps_trade_off', methods=['POST'])
def maps_trade_off():
    maps = GoogleMaps()
    return maps.trade_off_analytics(request.form["lat"], request.form["long"], request.form["dest"])


@app.route('/conversation_test', methods=['POST'])
def conversation_test():
    conversation = FarmerConversation()
    return conversation.converse(request.form["text"])


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(port))
