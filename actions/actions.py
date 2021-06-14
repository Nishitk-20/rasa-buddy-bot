# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class TeamProfile(Action):

    def name(self) -> Text: 
        return "action_team_profile"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        team = [
                {
                    "no" : "1",
                    "name" : "Soft Eng 1",
                    "manager" : "Manvendra",
                    "sendev" : ["Aditya","Archi"],
                    "jundev" : "Abhishek",
                    "intern" : "Dhairya"
                },
                {
                    "no": "2",
                    "name" : "Soft Eng 2",
                    "manager" : "Muskan",
                    "sendev" : ["Ganesh","Krishna"],
                    "jundev" : "Raj",
                    "intern" : "Alvin"

                },
                {
                    "no": "3",
                    "name" : "Soft Eng 3",
                    "manager" : "Nishant",
                    "sendev" : ["Niket","Kishan"],
                    "jundev" : "Riya",
                    "intern" : "Madhur"
                },
        ]
        
        t_no = tracker.get_slot("team_no")
        print(t_no)
        t_no = int(t_no)
        # if t_no == '1' :
        dispatcher.utter_message(text="Here is your team brief")
        # dispatcher.utter_message(text=f"Team : {team[t_no-1]}")
        dispatcher.utter_message(text="Manager : "+team[t_no-1]['manager'])
        dispatcher.utter_message(text="Senior developer : "+team[t_no-1]['sendev'][0])
        dispatcher.utter_message(text="Senior developer : "+team[t_no-1]['sendev'][1])
        dispatcher.utter_message(text="junior developer : "+team[t_no-1]['jundev'])
        dispatcher.utter_message(text="intern : "+team[t_no-1]['intern'])

        return []

class EventFetch(Action):

    def name(self) -> Text: 
        return "action_event_fetch"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        file = open("ab.txt", 'r')
        p = file.read()
        print(p)
        # p=''
        dispatcher.utter_message(p)
        dispatcher.utter_message("For more info you can go to \nhttps://www.unisys.com/events")
        p=''
        return []
 