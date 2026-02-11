import os

from gendiff.parser import parse


def get_data(file_path):
    _, extension = os.path.splitext(file_path)
    format_name = extension[1:].lower()
    with open(file_path, 'r') as f:
        content = f.read()
    return parse(content, format_name)


def generate_diff(file_path1, file_path2):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    
    diff = {}
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    
    for key in keys:
        if key not in data1:
            diff[key] = {'status': 'added', 'value': data2[key]}
        elif key not in data2:
            diff[key] = {'status': 'removed', 'value': data1[key]}
        elif data1[key] == data2[key]:
            diff[key] = {'status': 'unchanged', 'value': data1[key]}
        else:
            diff[key] = {
                'status': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            }

    return format_diff(diff)


def to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def format_diff(diff):
    lines = ['{']
    for key in sorted(diff.keys()):
        item = diff[key]
        status = item['status']
        
        if status == 'added':
            lines.append(f"  + {key}: {to_str(item['value'])}")
        elif status == 'removed':
            lines.append(f"  - {key}: {to_str(item['value'])}")
        elif status == 'unchanged':
            lines.append(f"    {key}: {to_str(item['value'])}")
        elif status == 'changed':
            lines.append(f"  - {key}: {to_str(item['old_value'])}")
            lines.append(f"  + {key}: {to_str(item['new_value'])}")
            
    lines.append('}')
    return '\n'.join(lines)