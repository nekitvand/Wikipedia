import json
import os


def load_config():
    with open(os.path.abspath(r'..\qa_data.json'), encoding="UTF-8") as f:
            json_data = json.load(f)
            qa_data_dict = json_data["test_data"]
    return qa_data_dict

def load_animal_facts():
    with open(os.path.abspath(r'..\animal_facts.json'),encoding="UTF-8") as f:
        json_data = json.load(f)
    return json_data