import json

def generate_diff(file_path1, file_path2):
    with open(file_path1) as file1, open(file_path2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    print(data1)
    print(data2)
    
    diff = {}
    
    
    return diff