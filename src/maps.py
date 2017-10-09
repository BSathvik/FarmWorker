# -*- coding: utf-8 -*-
import json

import requests


class GoogleMaps:

    def __init__(self):
        pass

    def distance_json(self, latitude, longitude, destination_param):

        destination = (destination_param+"").replace(" ", "+")

        key = "AIzaSyA79fdTvjbYAJCx3CEzMe31PexdQZI9TZE"

        req = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?origins="+latitude+","+longitude+"&destinations="+destination+"&key="+key)
        data = json.loads(req.text)


        distance_str_km = data["rows"][0]["elements"][0]["distance"]["text"]
        time = data["rows"][0]["elements"][0]["duration"]["text"]

        distance = float(distance_str_km[:-3])

        json_data = {"d": distance, "t": time}


        return json.dumps(json_data)

    def trade_off_analytics(self, latitude, longitude, destination_param):

        destination = (destination_param + "").replace(" ", "+")

        key = "AIzaSyA79fdTvjbYAJCx3CEzMe31PexdQZI9TZE"

        req = requests.get(
            "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + latitude + "," + longitude + "&destinations=" + destination + "&key=" + key)
        data = json.loads(req.text)

        distance = data["rows"][0]["elements"][0]["distance"]["value"]
        time = data["rows"][0]["elements"][0]["duration"]["value"]

        json_data = {"d": distance, "t": time}

        return json.dumps(json_data)
