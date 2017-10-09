# -*- coding: utf-8 -*-
import json
import requests


class HindiEnglish:

    def __init__(self):
        pass

    def hindi_to_eng(self, hindi_text):

        req = requests.get(
            "https://translation.googleapis.com/language/translate/v2?key=AIzaSyA79fdTvjbYAJCx3CEzMe31PexdQZI9TZE&target=en&q="+hindi_text+"&format=text")

        data = json.loads(req.text)
        eng_text = data["data"]["translations"][0]["translatedText"]

        return eng_text


    def eng_to_hindi(self, eng_text):

        req = requests.get(
            "https://translation.googleapis.com/language/translate/v2?key=AIzaSyA79fdTvjbYAJCx3CEzMe31PexdQZI9TZE&target=hi&q=" + eng_text + "&format=text")

        data = json.loads(req.text)
        hindi_text = data["data"]["translations"][0]["translatedText"]

        return hindi_text

