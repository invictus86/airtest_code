import json

with open("./config.json", 'r') as load_f:
    load_dict = json.load(load_f)
    print(load_dict.get("data1"))
