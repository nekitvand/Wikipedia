import json


def load_config():
    with open (r'C:\Users\Nikita\PycharmProjects\Wikipedia\qa_data.json', encoding="UTF-8") as f:
            json_data = json.load(f)
            qa_data_dict = json_data["test_data"]
    return qa_data_dict

