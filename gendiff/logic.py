import json

def generate_diff(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

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