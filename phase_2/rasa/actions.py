from rasa_sdk import Action,Tracker
from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List
from rasa_sdk.executor import CollectingDispatcher

class Critical(Action):
   def name(self) -> Text:
      return "action_critical"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      # file = open('C:\\Users\\akash\\OneDrive\\Desktop\\rasa_severity\\critical.txt','a')
      # inp = tracker.latest_message['text']
      # file.write(inp)
      print("Hi")
      dispatcher.utter_message("Critical severity issue identified.")
      return []
      
class High(Action):
   def name(self) -> Text:
      return "action_high"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      # file = open('C:\\Users\\akash\\OneDrive\\Desktop\\rasa_severity\\high.txt','a')
      # inp = tracker.latest_message['text']
      # file.write(inp)
      dispatcher.utter_message("High severity issue identified.")
      return []

class Moderate(Action):
   def name(self) -> Text:
      return "action_moderate"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      # file = open('C:\\Users\\akash\\OneDrive\\Desktop\\rasa_severity\\moderate.txt','a')
      # inp = tracker.latest_message['text']
      # file.write(inp)
      dispatcher.utter_message("Moderate severity issue identified.")
      return []