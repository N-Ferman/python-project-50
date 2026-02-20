def to_str(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if not isinstance(value, dict):
        return str(value)
    
    indent = ' ' * (depth * 4)
    lines = []
    for key, val in value.items():
        lines.append(f"{indent}    {key}: {to_str(val, depth + 1)}")
    result = '\n'.join(lines)
    return f"{{\n{result}\n{indent}}}"