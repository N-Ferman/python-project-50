import os
from gendiff.parser import parse

def get_data(file_path):
    
    _, extension = os.path.splitext(file_path)
    data_format = extension[1:].lower()
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    return parse(content, data_format)

def generate_diff(file_path1, file_path2):
    
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    diff = {}
    keys = set(data1.keys()) | set(data2.keys())
    for key in keys:
        if key in data1 and key not in data2:
            diff[key] = {'status': 'removed', 'value': data1[key]}
        elif key not in data1 and key in data2:
            diff[key] = {'status': 'added', 'value': data2[key]}
        elif data1[key] != data2[key]:
            diff[key] = {
                'status': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            }
        else:
            diff[key] = {'status': 'unchanged', 'value': data1[key]}
    return diff