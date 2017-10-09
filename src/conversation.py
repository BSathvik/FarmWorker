# -*- coding: utf-8 -*-
import base64
import json

from watson_developer_cloud import ConversationV1


class FarmerConversation:
    def __init__(self):
        pass

    def converse(self, text):

        conversation = ConversationV1(
            username='a5f91c9c-12e8-4809-9172-6f68ed4b01d3',
            password='mLvAkRPDUWZm',
            version='2016-09-20')

        workspace_id = '769ec18f-f67b-4d40-9611-8ce3487545da'

        response = conversation.message(workspace_id=workspace_id, message_input={'text': text})

        print json.dumps(response)

        intent = response["intents"][0]["intent"]

        if intent == "TipOfTheDay" or intent == "NewWord":
            entity_type = "None"
            entity_value = "None"
        else:
            entity_type = response["entities"][0]["entity"]
            entity_value = response["entities"][0]["value"]


        data_json = {"intent": intent, "entity_type": entity_type, "entity_value": entity_value}


        return json.dumps(data_json)
