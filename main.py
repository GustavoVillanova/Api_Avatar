import requests, json

def show_page():
    api_url = f'https://last-airbender-api.fly.dev/api/v1/characters'

    response = requests.get(api_url).json()

    for dict in response:
        for item in dict:
            print(item,'|',dict[item])

show_page()

