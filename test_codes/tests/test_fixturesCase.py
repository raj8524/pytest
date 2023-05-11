"""
its for DB connection or request connection or setup connection or close the connection.
"""
import json
import os
from test_codes.python_codes.fixtures_case import save_dict

#we need to pass builtin pytest fixtures(tempdir) as parameter to the function
#tmpdir is to create temp directory
#capsys is to check print statement written in function,validate the value
def test_save_dict(tmpdir, capsys):
    filepath = os.path.join(tmpdir, "test.json")
    _dict = {"a": 1, "b": 2}

    save_dict(_dict, filepath)
    assert json.load(open(filepath, 'r')) == _dict
    assert capsys.readouterr().out == "saved\n"