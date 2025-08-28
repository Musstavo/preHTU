import requests

base_url = "https://reqres.in/api"
headers = {
    "x-api-key": "reqres-free-v1"
}

def get_user_info(name):
    url = f"{base_url}/users/{name}"
    response = requests.get(url, headers=headers)
    status_code = response.status_code
    if status_code == 200:
        return response.json()
    else:
        print(f"Oh no.. it's down down {status_code}")

user = input("User name: ")
user_info = get_user_info(user)

if user_info:
    print(user_info["data"]["id"])
    print(user_info["data"]["email"])
    print(user_info["data"]["first_name"])
    print(user_info["data"]["last_name"])
    print(user_info["data"]["avatar"])
