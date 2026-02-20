from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain

def get_formatter(format_name):
    if format_name == 'stylish':
        return format_stylish
    if format_name == 'plain':
        return format_plain
    raise ValueError(f"Unknown format: {format_name}")