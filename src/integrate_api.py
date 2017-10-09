# -*- coding: utf-8 -*-

import json

from src.conversation import FarmerConversation
from src.crop_info import Crop_Info
from src.crop_price_dist import Crop_Price
from src.tip_of_day import Tip_Of_Day
from src.translation import HindiEnglish
from src.weather import WeatherYahoo
from src.word_of_the_day import Word_Of_The_Day


class Integrate_API:
    hindi_query = ""
    latitude = ""
    longitude = ""
    number = ""
    is_persist = ""
    reply_str = ""

    def __init__(self, sms_text, number):

        json_sms = json.loads(sms_text)

        self.hindi_query = json_sms["text"] + ""
        self.latitude = json_sms["lat"] + ""
        self.longitude = json_sms["long"] + ""
        self.is_persist = json_sms["per"] + ""

        self.number = number

    def start(self):

        # Translate from Hindi
        translate = HindiEnglish()
        eng_query = translate.hindi_to_eng(self.hindi_query)

        # Get Intent and entity conversation
        conversation = FarmerConversation()
        str_intent_entity_json = conversation.converse(eng_query)

        print eng_query + " :: " + str_intent_entity_json

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
                    print self.reply_str


                if entity_value == "today":
                    if self.is_persist == "true":
                        self.reply_str = (weather.get_json_weather_one_day() + "").replace("we1", "pwe1")
                    else:
                        self.reply_str = weather.get_json_weather_one_day()


                if entity_value == "day after":
                    self.reply_str = weather.get_json_weather_specific_day(2)
                    print self.reply_str

                if entity_value == "next three days":
                    self.reply_str = weather.get_json_weather_three_days()

        if intent == "SellPlacePrice":
            crop_price = Crop_Price()

            if entity_type == "crop":
                self.reply_str = crop_price.get_prices_in_cities(entity_value, self.latitude, self.longitude)

        if intent == "TipOfTheDay":

            tod = Tip_Of_Day()
            self.reply_str = tod.get_tip_of_day()

        if intent == "NewWord":

            wod = Word_Of_The_Day()
            self.reply_str = wod.get_word_of_day()

        if intent == "CropInfo":
            if entity_type == "crop":
                crop_info = Crop_Info()
                self.reply_str = crop_info.get_crop_info(entity_value)



        return self.reply_str

