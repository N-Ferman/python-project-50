import os

from gendiff.parser import parse
from gendiff.tree import build_diff_tree
from gendiff.formatters.stylish import format_stylish


def get_data(file_path):
    _, extension = os.path.splitext(file_path)
    format_name = extension[1:].lower()
    with open(file_path, 'r') as f:
        content = f.read()
    return parse(content, format_name)


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse(file_path1)
    data2 = parse(file_path2)
    diff_tree = build_diff_tree(data1, data2)

    selected_formatter = get_formatter(format_name)
    return selected_formatter(diff_tree)

   


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

def build_diff_tree(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    tree = []

    for key in keys:
        if key not in data1:
            tree.append({'key': key, 'type': 'added', 'value': data2[key]})
        elif key not in data2:
            tree.append({'key': key, 'type': 'removed', 'value': data1[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            children = build_diff_tree(data1[key], data2[key])
            tree.append({'key': key, 'type': 'nested', 'children': children})
        elif data1[key] == data2[key]:
            tree.append({'key': key, 'type': 'unchanged', 'value': data1[key]})
        else:
            tree.append({
                'key': key,
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })
    return tree