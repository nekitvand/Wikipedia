import requests


class Facts:

    def __init__(self,facts):
        self.facts = facts

    def cat(self):
        query = {"animal_type":"cat","amount":"2"}
        response = requests.get("https://cat-fact.herokuapp.com/facts/random", params=query)
        assert response.status_code == 200
        return response.json()

    def dog(self):
        query = {"animal_type":"dog","amount":"2"}
        response = requests.get("https://cat-fact.herokuapp.com/facts/random", params=query)
        assert response.status_code == 200
        return response.json()


