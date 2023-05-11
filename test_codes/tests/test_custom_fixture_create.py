"""default scope of custom fixture is function which means everytime object will be called when function is called.
whenever unittest is dependent on other func then,better to keep scope as function but its not advisable to mke
unitest dependent on other function.

we can keep scope as module when we want fixture (object) only once but use multiple times.
"""
from datetime import datetime
import pytest
from test_codes.python_codes.custom_fixture_create import student

@pytest.fixture(scope="function")
def dummy_student():
    print("making dummy student")
    return student("nikhil", datetime(2000, 1, 1), "coe")


def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


def test_student_add_credits(dummy_student):
    dummy_student.add_credits(5)
    assert dummy_student.get_credits() == 5


def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 0