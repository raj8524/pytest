import pytest
from unittest import mock
from test_codes.python_codes.mock_dice_pro_sample import guess_number,get_ip

"""
#need to pass function in local scope of roll_dice.in this case guess_number (roll_device called into it). called
@mock.patch("test_codes.python_codes.mock_dice_pro_sample.roll_dice")
def test_guess_number(mock_roll_dice):
    mock_roll_dice.return_value=3
    assert guess_number(3) == "You won!"
"""

#parametrizing the mock behaviour
@pytest.mark.parametrize("input1,expected", [(3, "You won!"), (4, "You lost!")])
@mock.patch("test_codes.python_codes.mock_dice_pro_sample.roll_dice")
def test_guess_number(mock_roll_dice):
    mock_roll_dice.return_value = 3
    assert guess_number(input1) == expected



@mock.patch("test_codes.python_codes.mock_dice_pro_sample.requests.get")
def test_get_ip(mock_requests_get):
    mock_requests_get.return_value = mock.Mock(name="mock response",
                                               **{"status_code": 200, "json.return_value": {"origin": "0.0.0.0"}})

    assert get_ip() == "0.0.0.0"
    mock_requests_get.assert_called_once_with("https://httpbin.org/ip")