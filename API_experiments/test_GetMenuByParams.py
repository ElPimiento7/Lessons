import requests
import json
import allure

api_key = "ZITf3wuLbEE=G2QqE7gcKKScM9/3YdKGgvVd/dpqSyyDfHTdLuILj3Y8FCnJnxtkP03LwmQb3p2eU2C3xQTm81Us4jdgWceKJ3k4FSIbE0s1Fs+b2brzfvjaCQ+HxT5bzL9cddjHUa9D7VRXLoTq22VA4CcekQJJNr9wst3SQ1kwwTNoB/a8DTadR7KMp6EHXADnMmRmBrDhfXbo2YuS9iKl4Cxl4nMao1IA2LRsMtMK"


@allure.feature("API Tests")
@allure.story("Get Menu by Params")
@allure.title("Check if response contains expected keys")
def test_get_menu_by_params():
    url = "https://ws-test.ucs.ru/wsserverlp/api/v2/aggregators/Create"
    headers = {
        "AggregatorAuthentication": api_key,
        "Content-Type": "application/json; charset=utf-8"
    }
    params = {
        "taskType": "GetMenuByParams",
        "params": {
            "sync": {
                "objectId": 199990377,
                "timeout": 120
            },
            "filterByKassPresets": True,
            "orderCategoryCode": 3
        }
    }
    response = requests.post(
        url=url,
        headers=headers,
        json=params
    )
    actual_response = response.json()

    expected_keys = ["taskGuid", "taskType", "objectId", "agentGuid"]
    assert response.status_code == 200
    assert all(key in actual_response.get("responseCommon", {}) for key in
               expected_keys), f"Отсутствуют ожидаемые ключи {expected_keys}"

    # print(response.status_code)
    # print(response.json())
    # formatted_json = json.dumps(response.json(), indent=4, ensure_ascii=False)
    # print(formatted_json)

# get_menu_by_params(api_key)
