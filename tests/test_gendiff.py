import pytest
import os
from gendiff import generate_diff

def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', file_name)


@pytest.mark.parametrize("file1, file2", [
    ('file1.json', 'file2.json'),
    ('file1.yml', 'file2.yml'),
])
def test_generate_diff(file1, file2):
    path1 = get_fixture_path(file1)
    path2 = get_fixture_path(file2)
    
    
    with open(get_fixture_path('expected.txt'), 'r') as f:
        expected = f.read().strip()
        
    assert generate_diff(path1, path2) == expected