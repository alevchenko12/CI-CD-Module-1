import pytest
import os
from main import write_to_file

@pytest.fixture
def temp_file(tmpdir):
    file_path = os.path.join(tmpdir, 'test_file.txt')
    yield file_path

def test_write_to_file(temp_file):
    lines = ['Line 1', 'Line 2', 'Line 3']

    write_to_file(temp_file, lines)
    
    with open(temp_file, 'r') as file:
        written_content = file.read().splitlines()
    
    assert written_content == lines
