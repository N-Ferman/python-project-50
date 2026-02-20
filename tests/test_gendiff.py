import pytest
from gendiff import generate_diff

def read_fixture(file_name):
    with open(f'tests/fixtures/{file_name}', 'r') as f:
        return f.read().strip()



def test_generate_diff_stylish(file1, file2, expected_file):
    path1 = f'tests/fixtures/{file1}'
    path2 = f'tests/fixtures/{file2}'
    expected = read_fixture(expected_file)
    assert generate_diff(path1, path2) == expected

@pytest.mark.parametrize('file1, file2, format, expected', [
    ('file1.json', 'file2.json', 'stylish', 'expected_stylish.txt'),
    ('file1.yml', 'file2.yml', 'stylish', 'expected_stylish.txt'),
    ('file1.json', 'file2.json', 'plain', 'expected_plain.txt'),
    ('file1.yml', 'file2.yml', 'plain', 'expected_plain.txt'),
])