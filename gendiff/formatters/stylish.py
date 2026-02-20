def to_str(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if not isinstance(value, dict):
        return str(value)

    indent_size = depth * 4
    current_indent = ' ' * indent_size
    bracket_indent = ' ' * ((depth - 1) * 4)
    lines = []
    for key, val in value.items():
        lines.append(f"{current_indent}{key}: {to_str(val, depth + 1)}")
    return '{\n' + '\n'.join(lines) + '\n' + bracket_indent + '}'


def format_stylish(tree, depth=1):
    lines = ['{']
    indent_size = depth * 4 - 2
    current_indent = ' ' * indent_size
    bracket_indent = ' ' * ((depth - 1) * 4)

    for node in tree:
        key = node['key']
        node_type = node['type']

        if node_type == 'added':
            lines.append(
                f"{current_indent}+ {key}: {to_str(node['value'], depth + 1)}"
            )
        elif node_type == 'removed':
            lines.append(
                f"{current_indent}- {key}: {to_str(node['value'], depth + 1)}"
            )
        elif node_type == 'unchanged':
            lines.append(
                f"{current_indent}  {key}: {to_str(node['value'], depth + 1)}"
            )
        elif node_type == 'changed':
            lines.append(
                f"{current_indent}- {key}: {to_str(node['old_value'], depth + 1)}"
            )
            lines.append(
                f"{current_indent}+ {key}: {to_str(node['new_value'], depth + 1)}"
            )
        elif node_type == 'nested':
            children_str = format_stylish(node['children'], depth + 1)
            lines.append(
                f"{current_indent}  {key}: {children_str}"
            )

    lines.append(bracket_indent + '}')
    return '\n'.join(lines)