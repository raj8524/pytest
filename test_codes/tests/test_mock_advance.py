import random,time,json,requests
import pytest
from unittest.mock import call
from unittest import mock
from test_codes.python_codes.mock_advanced import random_sum,silly


@mock.patch("test_codes.python_codes.mock_advanced.random.randint")
def test_random_sum(mock_randint):
    mock_randint.side_effect = [3, 4]
    assert random_sum() == 7
    mock_randint.assert_has_calls(calls=[call(1, 10), call(1, 7)])


@mock.patch("tut10.myapp.sample.random.randint")
@mock.patch("test_codes.python_codes.mock_advanced.time.time")
@mock.patch("test_codes.python_codes.mock_advanced.requests.get")
#mock object should be defined bottom-up approach
def test_silly(mock_requests_get, mock_time, mock_randint):
    test_params = {
        "timestamp": 123,
        "number": 5
    }
    mock_time.return_value = test_params['timestamp']
    mock_randint.return_value = 5
    mock_requests_get.return_value = mock.Mock(**{"status_code": 200,
                                                  "json.return_value":
                                                      {"args": test_params}})

    assert silly() == test_params
