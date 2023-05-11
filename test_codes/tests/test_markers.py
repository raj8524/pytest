import pytest
from test_codes.python_codes.markers import add
import sys
@pytest.mark.skip(reason="just wanna skip it")
def test_add_num():
    assert add(1, 2) == 3

#if condition matches ,then, it will be skipped(ignored)
@pytest.mark.skipif(sys.version_info > (3, 9), reason="use python 3.9 or less")
def test_add_str():
    assert add("a", "b") == "ab"


#if condition matches,exception is raised then, it will be skipped(ignored)
@pytest.mark.xfail(sys.platform == "win32", reason="dont run on windows")
def test_add_list():
    assert add([1], [2]) == [1, 2]
    raise Exception()
