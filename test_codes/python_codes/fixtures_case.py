"""
its for DB connection or request connection or setup connection or close the connection.
"""
import json
def save_dict(_dict, filepath):
    json.dump(_dict, open(filepath, 'w'))
    print("saved")
    