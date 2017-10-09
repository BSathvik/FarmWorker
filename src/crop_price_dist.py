# -*- coding: utf-8 -*-
import json

from mysql import connector
from watson_developer_cloud import TradeoffAnalyticsV1

from src.maps import GoogleMaps
from src.translation import HindiEnglish

conn = connector.connect(host='52.77.72.190',
                               database='farmers',
                               user='admin',
                               password='sATHVIk#)')


class Crop_Price:

    def __init__(self):
        pass


    def get_prices_in_cities(self, crop_name, lat, long):

        cur = conn.cursor()
        cur.execute("SELECT * FROM Veg_Prices WHERE C2 LIKE '" + crop_name + "'")

        row = cur.fetchone()

        price_city_data = []

        count = 1

        while row is not None:

            place = row[0]
            maps = GoogleMaps()
            dist = (json.loads(maps.distance_json(lat, long, place))["d"])

            price_city_data.append({"key": str(count), "name":row[0], "values":{"dist": dist, "price": row[2]}  })

            count += 1

            row = cur.fetchone()


        columns = [{"key":"price", "type":"numeric", "goal":"max", "is_objective":True, "full_name":"Price", "range":{"low":0, "high":1000}},
                    {"key":"dist", "type":"numeric", "goal":"min", "is_objective":True, "full_name":"Distance", "range":{"low":0, "high":1000}}]

        final_trade_off_request = {"subject":"farmers_optimum_selling", "columns": columns, "options":price_city_data}

        tradeoff_analytics = TradeoffAnalyticsV1(
            username='c32f6737-b004-4e21-baf7-1d684d0feb39',
            password='iMVJznCBsN6t')

        dilemma = tradeoff_analytics.dilemmas(final_trade_off_request, generate_visualization=False)

        json_response = json.dumps(self.parse_json_trade_sol(dilemma, crop_name))

        return json_response


    def parse_json_trade_sol(self, solution, crop_name):

        answer_json = {}

        final_solution_value_ref = ""

        trans = HindiEnglish()

        for cur_sol in solution["resolution"]["solutions"]:
            if cur_sol["status"] == "FRONT":
                final_solution_value_ref = cur_sol["solution_ref"]

        for cur_value in solution["problem"]["options"]:
            if cur_value["key"] == final_solution_value_ref:
                answer_json.update({"crn":trans.eng_to_hindi(crop_name), "ty":"pcpr1" ,"cn":trans.eng_to_hindi(cur_value["name"]), "pr":cur_value["values"]["price"], "di":cur_value["values"]["dist"]})

        return answer_json

