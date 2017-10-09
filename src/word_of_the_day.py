# -*- coding: utf-8 -*-
import json
from random import randint




class Word_Of_The_Day:
    def __init__(self):
        pass

    def get_word_of_day(self):

        wods = [{"w_e":"quantity", "h_w":"मात्रा"}]


        index = randint(0, wods.__len__() -1)

        sentence = "दिन के शब्द '"+wods[index]["w_e"]+"' है और इसका अर्थ "+wods[index]["h_w"]+" है"

        print sentence

        return json.dumps({"ty":"pwod", "tp":sentence})



wod = Word_Of_The_Day()
print wod.get_word_of_day()
