from datetime import datetime
import pytest
from test_codes.python_codes.custom_fixture_factory import Student,get_topper

#this is how we create  NORMAL fixture .
@pytest.fixture()
def dummy_student():
    print("making dummy student")
    return Student("nikhil", datetime(2000, 1, 1), "coe",20)


#this is how we create fixture factory.
@pytest.fixture()
def dummy_student_factory():

    def make_dummy_students(name,credits):
        return Student(name, datetime(2000, 1, 1), "coe",credits)
    return make_dummy_students

def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age


def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 20


def test_get_topper(dummy_student_factory):
    students = [
        dummy_student_factory("ram", 21),
        dummy_student_factory("shyam", 19),
        dummy_student_factory("ravi", 22)
    ]

    topper = get_topper(students)

    assert topper == students[2]