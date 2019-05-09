import requests
import pytest
import json

class Facts:

    def __init__(self,facts):
        self.facts = facts

    def cat(self):
        query = {"animal_type":"cat","amount":"2"}
        response = requests.get("https://cat-fact.herokuapp.com/facts/random", params=query)
        response_response = response.json()
        assert response_response[0]["type"] == "cat"
        return response.json()


