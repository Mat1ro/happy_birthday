import json


def load_congratulations():
    with open('./data/congratulations.json', 'r', encoding='utf-8') as file:
        return json.load(file)


