import requests, pandas

def show_page():
    page = requests.get("https://last-airbender-api.fly.dev/api/v1/characters")
    return print(page.json())

show_page()