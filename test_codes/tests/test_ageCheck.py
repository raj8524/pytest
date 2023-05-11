import pytest
from test_codes.python_codes.ageCheck import validate_age


def test_validate_age_valid_age():
    validate_age(10)


def test_validate_age_invalid_age():
    with pytest.raises(ValueError, match="Age cannot be less than 0"):
        #same MATCH comment defined in agecheck function
        validate_age(-1)