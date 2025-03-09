import requests

def convert_api(currency_base, currency_target):
    link = f"https://economia.awesomeapi.com.br/last/{currency_base}-{currency_target}"
    api = requests.get(link)

    conversion = api.json()[f"{currency_base}{currency_target}"]["bid"]
    return conversion