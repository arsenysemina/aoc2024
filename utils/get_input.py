import os
from pathlib import Path

import requests
from dotenv import dotenv_values
session = dotenv_values(".env")['session']

def get_input(day):
    input_path = Path(f"day{day}/data.txt")
    if input_path.exists():
        with open(input_path, "r") as f:
            return f.read()
    else:
        url = f"https://adventofcode.com/2024/day/{day}/input"
        cookies = {"session": session}
        res = requests.get(url, cookies=cookies)
        res.raise_for_status()
        data = res.text
        with open(input_path, "w") as f:
            f.write(data)
        return data