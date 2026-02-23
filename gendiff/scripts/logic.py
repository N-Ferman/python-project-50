import os

from gendiff.formatters import get_formatter

from .parser import parse


def get_data(file_path):
    _, extension = os.path.splitext(file_path)
    format_name = extension[1:].lower()
    with open(file_path, "r") as f:
        content = f.read()
    return parse(content, format_name)


def generate_diff(file_path1, file_path2, format_name="stylish"):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    diff_tree = build_diff_tree(data1, data2)
    formatter = get_formatter(format_name)
    return formatter(diff_tree)


def build_diff_tree(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    tree = []
    for key in keys:
        if key not in data1:
            tree.append({"key": key, "type": "added", "value": data2[key]})
        elif key not in data2:
            tree.append({"key": key, "type": "removed", "value": data1[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            children = build_diff_tree(data1[key], data2[key])
            tree.append({"key": key, "type": "nested", "children": children})
        elif data1[key] == data2[key]:
            tree.append({"key": key, "type": "unchanged", "value": data1[key]})
        else:
            tree.append(
                {
                    "key": key,
                    "type": "changed",
                    "old_value": data1[key],
                    "new_value": data2[key],
                }
            )
    return tree
