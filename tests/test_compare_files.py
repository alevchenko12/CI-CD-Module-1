import os
import pytest
from main import compare_files

@pytest.fixture
def create_temp_files(tmpdir):
    file1_content = """Line 1
    Line 2
    Line 3"""
    file2_content = """Line 1
    Line 4
    Line 5"""
    
    file1_path = os.path.join(tmpdir, 'file1.txt')
    with open(file1_path, 'w') as file1:
        file1.write(file1_content)
    
    file2_path = os.path.join(tmpdir, 'file2.txt')
    with open(file2_path, 'w') as file2:
        file2.write(file2_content)
    
    return file1_path, file2_path

def test_compare_files(create_temp_files):    
    file1_path, file2_path = create_temp_files
    
    compare_files(file1_path, file2_path)
    
    same_file_path = os.path.join('same.txt')
    diff_file_path = os.path.join('diff.txt')
    assert os.path.exists(same_file_path)
    assert os.path.exists(diff_file_path)
    
    with open(same_file_path, 'r') as same_file:
        same_content = same_file.read().splitlines()
    with open(diff_file_path, 'r') as diff_file:
        diff_content = diff_file.read().splitlines()
    
    assert same_content == ['Line 1']
    assert diff_content == ['Line 2', 'Line 3', 'Line 4', 'Line 5']
