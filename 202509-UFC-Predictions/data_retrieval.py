import json 
import pandas as pd
import os

# json retrieval function
def retrieve_json(data_folder='data'):
    """
    @desc: Loops through all JSON files in the data folder and loads them into a dictionary.
    @returns: a dic with filenames as keys and loaded JSON as values
    """
    json_data = {}
    for filename in os.listdir(data_folder):
        if filename.endswith('.json'):
            filepath = os.path.join(data_folder, filename)
            with open(filepath, 'r') as f:
                json_data[filename] = json.load(f)
    return json_data

# load all json files into the environment as a dictionary
json_dict = retrieve_json()
print(json_dict.keys())




