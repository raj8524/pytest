import pytest
from test_codes.python_codes.parametrised_case import add
def test_add_num():
    assert add(1, 2) == 3


def test_add_str():
    assert add("a", "b") == "ab"


def test_add_list():
    assert add([1, 2], [3]) == [1, 2, 3]


@pytest.mark.parametrize("a,b,c", [(1, 2, 3), ("a", "b", "ab"),
                                   ([1, 2], [3], [1, 2, 3])],
                         ids=["num", "str", "list"])
#in the list values r for a,b,c. All above 3 cases r covered in line 15 parametrised
def test_add(a, b, c):
    assert add(a, b) == c