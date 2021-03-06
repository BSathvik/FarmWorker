# -*- coding: utf-8 -*-
import json
from random import randint


class Tip_Of_Day:

    def __init__(self):
        pass


    def get_tip_of_day(self):

        tips = ["नियमित रूप से कीट के लिए जाँच करने के लिए सुनिश्चित करें।",
                "आसपास के उपकरण या काम क्षेत्रों ढीले कपड़े न पहनें।",
                "दस्ताने, सुनवाई के संरक्षण, सुरक्षा आंख पहनने, चेहरे मास्क, और respirators का प्रयोग करें।",
                "जब अनाज डिब्बे, प्रजनन कलम या अन्य उच्च जोखिम वाले क्षेत्रों में प्रवेश हमेशा पास एक सहायक है।",
                "ट्रैक्टर संलग्नक और औजार पर सवार निषेध।",
                "ट्रैक्टर और आग बुझाने और प्राथमिक चिकित्सा किट के साथ खेत ट्रकों संगठन।",
                "कभी बिजली उपकरण पहुंच से बाहर चल छोड़।",
                "चेक करें और पाइप और दरारें या पहनने के अन्य लक्षण दिखा बिजली के तारों की तरह उपकरण बनाए रखें।",
                "अच्छे स्वास्थ्य में जानवरों रखें। दर्द और बेचैनी में एक जानवर आक्रामक तरीके से प्रतिक्रिया कर सकते हैं।"]



        index = randint(0, tips.__len__() -1)

        return json.dumps({"ty":"ptod", "tp":tips[index]})
