import pytest
import os
from main import read_file

@pytest.fixture
def create_temp_file(tmpdir):
    file_content = """Line 1
    Line 2
    Line 3"""    
    
    file1_path = os.path.join(tmpdir, 'test_file1.txt')   
    with open(file1_path, 'w') as file1:
        file1.write(file_content)  
    
    return file1_path

def test_read_file(create_temp_file):    
    temp_file_path = create_temp_file
    result = read_file(temp_file_path)
    
    expected_content = {'Line 1', 'Line 2', 'Line 3'}
    
    assert result == expected_content
