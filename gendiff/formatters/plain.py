def to_str(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, int):
        return str(value) 
    return f"'{value}'"

def format_plain(diff_tree):
    def walk(node, path):
        lines = []
        for item in node:
            current_path = f"{path}{item['key']}"
            node_type = item['type']

            if node_type == 'nested':
                lines.append(walk(item['children'], f"{current_path}."))
            
            elif node_type == 'added':
                val = to_str(item['value'])
                lines.append(f"Property '{current_path}' was added with value: {val}")
            
            elif node_type == 'removed':
                lines.append(f"Property '{current_path}' was removed")
            
            elif node_type == 'changed':
                val1 = to_str(item['old_value'])
                val2 = to_str(item['new_value'])
                lines.append(f"Property '{current_path}' was updated. From {val1} to {val2}")
        return "\n".join(lines)

    return walk(diff_tree, "")