import json


FILENAME = "response.json"

FIELD_LIST = ["taskGuid", "taskType", "objectId", "agentGuid"]


def read(FILENAME, FIELD_LIST):
    with open(FILENAME, "r") as json_file:
        json_data = json.load(json_file)["responseCommon"]
        result = []
        for field in FIELD_LIST:
            result.append({field: json_data[field]})
        return result


if __name__ == "__main__":
    print(read(FILENAME, FIELD_LIST))