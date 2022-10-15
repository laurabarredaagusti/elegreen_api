from flask import jsonify
import json
from variables import *

class Calculate:
    store_data_path = store_data_path
    def __init__(self, session_id, arguments_list):

        self.arguments_list = arguments_list
        
        self.session_id = session_id
        self.hours_day = float(arguments_list[2])
        self.price_kwh = float(arguments_list[3])
        self.current_datetime = arguments_list[4]
        
        self.calculate()
        self.get_dict()
        self.get_json()
        self.read_data_json()
        self.store_data_dict()
        self.update_json()

    def calculate(self):
        self.cost = self.price_kwh * self.hours_day

    def get_dict(self):
        self.dict = {'Cost': str(self.cost)}

    def get_json(self):
        self.json = jsonify(self.dict)

    def read_data_json(self):
        with open(self.store_data_path, 'r') as j:
            self.contents = json.loads(j.read())

    def store_data_dict(self):
        self.arguments_list.append(self.cost)
        self.data_dict = {}
        for index, data in enumerate(store_data):
            self.data_dict[data] = self.arguments_list[index]

    def update_json(self):
        self.contents[self.session_id] = self.data_dict
        with open(self.store_data_path, 'w') as outfile:
            json.dump(self.contents, outfile)

