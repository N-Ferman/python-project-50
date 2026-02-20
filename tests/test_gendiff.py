from pathlib import Path

import pytest

from gendiff import generate_diff


FIXTURES_DIR = Path(__file__).parent / 'fixtures'


def read_fixture(file_name: str) -> str:
    return (FIXTURES_DIR / file_name).read_text().strip()


@pytest.mark.parametrize(
    'file1,file2,format_name,expected_fixture',
    [
        ('file1.json', 'file2.json', 'stylish', 'expected_stylish.txt'),
        ('file1.yml', 'file2.yml', 'stylish', 'expected_stylish.txt'),
        ('file1.json', 'file2.json', 'plain', 'expected_plain.txt'),
        ('file1.yml', 'file2.yml', 'plain', 'expected_plain.txt'),
    ],
)
def test_generate_diff(file1, file2, format_name, expected_fixture):
    path1 = str(FIXTURES_DIR / file1)
    path2 = str(FIXTURES_DIR / file2)
    expected = read_fixture(expected_fixture)
    assert generate_diff(path1, path2, format_name) == expected