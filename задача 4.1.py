
import json


FILENAME = "input.json"


def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)
        list_values = [item["score"] * item["weight"] for item in json_data]
        s = sum(list_values)
    return round(s, 3)


print(task())
