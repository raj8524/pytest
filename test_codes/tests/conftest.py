from datetime import datetime
import pytest
from test_codes.python_codes.parametrized_fixtures import Student,is_eligible_for_degree



@pytest.fixture
def dummy_student(request):
    return Student("nikhil", datetime(2000, 1, 1), "coe", request.param)


@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), "coe", credits)

    return _make_dummy_student