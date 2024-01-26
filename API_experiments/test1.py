import requests
import json

# GET
def get_all_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    for x in response:
        print(x["title"])


def get_one_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/77").json()
    print(response)


# POST
def post_new_post():
    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }
    body = json.dumps({
        "title": "foo",
        "body": "bar",
        "userId": 1
    })
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        data=body,
        headers=headers
    )
    print(response.status_code)
    print(response.json())


# PUT
def update_one_post():
    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }
    body = json.dumps({
        "title": "foo1",
        "body": "bar2",
        "userId": 1
    })
    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/77",
        data=body,
        headers=headers
    )
    print(response.status_code)
    print(response.json())


# PATCH
def patch_one_post():
    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }
    body = json.dumps({
        "body": "bar2",
        "userId": 1
    })
    response = requests.patch(
        "https://jsonplaceholder.typicode.com/posts/77",
        data=body,
        headers=headers
    )
    print(response.status_code)
    print(response.json())


# DELETE
def delete_one_post():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/77")
    print(response.status_code)
    print(response.json())


delete_one_post()