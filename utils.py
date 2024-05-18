import json


def check_if_config_exists():
    try:
        with open("config.json", "r") as _:
            return True
    except FileNotFoundError:
        return False


def load_token():
    with open("config.json", "r") as file:
        return json.load(file)["token"]


def load_prefix():
    with open("config.json", "r") as file:
        return json.load(file)["prefix"]
