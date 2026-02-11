import json
import yaml

def parse(data, format_name):
    if format_name == 'json':
        return json.loads(data)
    if format_name in ('yml', 'yaml'):
        return yaml.safe_load(data)
    raise ValueError(f"Unknown format: {format_name}")