from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from .json import format_json

def get_formatter(format_name):
    if format_name == 'stylish':
        return format_stylish
    if format_name == 'plain':
        return format_plain
    if format_name == 'json':
        return format_json
    raise ValueError(f"Unknown format: {format_name}")