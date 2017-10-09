# -*- coding: utf-8 -*-
import json

from mysql import connector

from src.translation import HindiEnglish

conn = connector.connect(host='52.77.72.190',
                         database='farmers',
                         user='admin',
                         password='sATHVIk#)')


class Crop_Info:
    def __init__(self):
        pass

    def get_crop_info(self, crop_name):
        cur = conn.cursor()

        cur.execute("SELECT * FROM Cultivationdetails WHERE C1 LIKE '" + crop_name + "'")

        row = cur.fetchone()

        crop_info_array = {"ty": "crin", "data": {}}

        count = 1

        translate = HindiEnglish()

        while row is not None:
            cr_crp_name = translate.eng_to_hindi(row[0])
            cr_temp = translate.eng_to_hindi(row[1])
            cr_soil = translate.eng_to_hindi(row[2])
            cr_manure = translate.eng_to_hindi(row[3])
            cr_pests = translate.eng_to_hindi(row[4])
            cr_diseases = translate.eng_to_hindi(row[5])
            cr_water = row[6]
            cr_drainage = row[7]
            cr_file_name = row[8]


            crop_info_array["data"] = {"na_c": cr_crp_name, "temp": cr_temp, "soil": cr_soil, "man": cr_manure,
                                       "pes": cr_pests, "dis": cr_diseases, "wat": cr_water, "dra": cr_drainage, "ic":cr_file_name}

            count += 1

            row = cur.fetchone()

        return json.dumps(crop_info_array)


#cr = Crop_Info()
#print cr.get_crop_info("Rice")
