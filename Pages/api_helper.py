import requests


class Facts:


    def __init__(self,facts):
        self.facts = facts
        self.text_to_translate = None

    def cat(self):
        query = {"animal_type":"cat","amount":"2"}
        response = requests.get("https://cat-fact.herokuapp.com/facts/random", params=query)
        self.text_to_translate = [response.json()[0].get("text"), response.json()[1].get("text")]
        assert response.status_code == 200
        return response.json()

    def dog(self):
        query = {"animal_type":"dog","amount":"2"}
        response = requests.get("https://cat-fact.herokuapp.com/facts/random", params=query)
        dogs_facts = [response.json()[0].get("text") , response.json()[1].get("text")]
        self.text_to_translate.extend(dogs_facts)
        assert response.status_code == 200
        return response.json()

    def yandex_translate(self):
        KEY = "trnsl.1.1.20190115T093726Z.65e1460d8d95bd06.852e4ad5c304d72e8606055f595bcea9f3cf8001"
        text = self.text_to_translate
        query = {
            "key": KEY,
            "text": text,
            "lang": 'en-ru'
        }
        response = requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate",params=query)
        return response.json()


    def yandex_translate_multilang(self,lang,text):
        KEY = "trnsl.1.1.20190115T093726Z.65e1460d8d95bd06.852e4ad5c304d72e8606055f595bcea9f3cf8001"
        query = {
            "key": KEY,
            "text": text,
            "lang": lang
        }
        response = requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate",params=query)
        return response.json()