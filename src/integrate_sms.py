# -*- coding: utf-8 -*-
import base64
import json

import requests

from src.conversation import FarmerConversation
from src.crop_info import Crop_Info
from src.crop_price_dist import Crop_Price
from src.tip_of_day import Tip_Of_Day
from src.translation import HindiEnglish
from src.weather import WeatherYahoo
from src.word_of_the_day import Word_Of_The_Day


class Integrate_SMS:
    hindi_query = ""
    latitude = ""
    longitude = ""
    number = ""
    is_persist = ""
    reply_str = ""

    def __init__(self, sms_text, number):


        json_sms = json.loads(self.convert_sms_to_json(sms_text))

        self.hindi_query = base64.b64decode(json_sms["text"])
        self.latitude = json_sms["lat"] + ""
        self.longitude = json_sms["long"] + ""
        self.is_persist = json_sms["per"] + ""
        self.number = number


    def convert_json_to_sms(self, sms):
        sms_01 = str(sms).replace("{", "<")
        sms_02 = str(sms_01).replace("}", ">")

        return sms_02


    def convert_sms_to_json(self, json_txt):
        txt_01 = str(json_txt).replace("<", "{")
        txt_02 = str(txt_01).replace(">", "}")

        return txt_02

    def send_sms(self, text):

        req = requests.post("https://api.textlocal.in/send", data={"username": "sathvikbiradavolu@gmail.com",
                                                                   "hash": "54433e2d94aa89ff1da199d76bab4fd725412245",
                                                                   "sender": "TXTLCL",
                                                                   "message": self.convert_json_to_sms(text) + "",
                                                                   "numbers": self.number + "",
                                                                   "test": "false",
                                                                   "unicode": "true"})
        print req

    def start(self):

        # Translate from Hindi
        translate = HindiEnglish()
        eng_query = translate.hindi_to_eng(self.hindi_query)

        # Get Intent and entity conversation
        conversation = FarmerConversation()
        str_intent_entity_json = conversation.converse(eng_query)

        intent_entity_json = json.loads(str_intent_entity_json)

        intent = intent_entity_json["intent"]
        entity_type = intent_entity_json["entity_type"]
        entity_value = intent_entity_json["entity_value"]

        # Do something with these requests
        if intent == "Weather":

            weather = WeatherYahoo(self.latitude, self.longitude)

            if entity_type == "Weather_Days":
                if entity_value == "tomorrow":
                    self.reply_str = weather.get_json_weather_specific_day(1)
                    self.send_sms(self.reply_str)

                if entity_value == "today":
                    if self.is_persist == "true":
                        self.reply_str = (weather.get_json_weather_one_day() + "").replace("we1", "pwe1")
                    else:
                        self.reply_str = weather.get_json_weather_one_day()

                    self.send_sms(self.reply_str)

                if entity_value == "day after":
                    self.reply_str = weather.get_json_weather_specific_day(2)
                    self.send_sms(self.reply_str)

                if entity_value == "next three days":
                    self.reply_str = weather.get_json_weather_three_days()
                    self.send_sms(self.reply_str)

        if intent == "SellPlacePrice":
            crop_price = Crop_Price()

            if entity_type == "crop":

                self.reply_str = crop_price.get_prices_in_cities(entity_value, self.latitude, self.longitude)
                self.send_sms(self.reply_str)


        if intent == "TipOfTheDay":
            tod = Tip_Of_Day()
            self.reply_str = tod.get_tip_of_day()
            self.send_sms(self.reply_str)


        if intent == "NewWord":
            wod = Word_Of_The_Day()
            self.reply_str = wod.get_word_of_day()
            self.send_sms(self.reply_str)

        if intent == "CropInfo":
            if entity_type == "crop":
                crop_info = Crop_Info()
                self.reply_str = crop_info.get_crop_info(entity_value)
                self.send_sms(self.reply_str)

        return self.reply_str
