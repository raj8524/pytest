from datetime import datetime
import pytest
from test_codes.python_codes.parametrized_fixtures import Student,is_eligible_for_degree

#conftest.py contains fixtures for this .
"""
# same is written in conftest.py
@pytest.fixture
def dummy_student(request):
    return Student("nikhil", datetime(2000, 1, 1), "coe", request.param)


@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000, 1, 1), "coe", credits)

    return _make_dummy_student
"""

def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


def test_student_is_eligible_for_degree_false(make_dummy_student):
    assert is_eligible_for_degree(make_dummy_student("sam", 19)) is False


def test_student_is_eligible_for_degree_true(make_dummy_student):
    assert is_eligible_for_degree(make_dummy_student("sam", 21)) is True


@pytest.mark.parametrize("credits,expected", [(19, False), (21, True)])
def test_student_is_eligible_for_degree(make_dummy_student, credits, expected):
    assert is_eligible_for_degree(make_dummy_student("sam", credits)) is expected


#this doesnt require fixture factory.
@pytest.mark.parametrize("dummy_student,expected", [(19, False), (21, True)],
                         indirect=["dummy_student"],
                         ids=["ineligible", "eligible"])
def test_student_is_eligible_for_degree(dummy_student, expected):
    assert is_eligible_for_degree(dummy_student) is expected