import pytest
from gendiff import generate_diff

def read_fixture(file_name):
    with open(f'tests/fixtures/{file_name}', 'r') as f:
        return f.read().strip()

@pytest.mark.parametrize('file1, file2, expected_file', [
    ('file1.json', 'file2.json', 'result_stylish.txt'),
    ('file1.yml', 'file2.yml', 'result_stylish.txt'),
])

def test_generate_diff_stylish(file1, file2, expected_file):
    path1 = f'tests/fixtures/{file1}'
    path2 = f'tests/fixtures/{file2}'
    expected = read_fixture(expected_file)
    assert generate_diff(path1, path2) == expected