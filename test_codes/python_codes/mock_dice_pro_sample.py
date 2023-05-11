import requests

from test_codes.python_codes.mock_dice_pro1 import roll_dice

def guess_number(num):
    result = roll_dice()
    if result == num:
        return "You won!"
    else:
        return "You lost!"


def get_ip():
    response = requests.get("https://httpbin.org/ip")
    if response.status_code == 200:
        return response.json()['origin']