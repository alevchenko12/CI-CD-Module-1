import pytest
from main import compare_cycle

@pytest.fixture
def empty_sets():
    return set(), set()

@pytest.fixture
def one_empty_set():
    return {'line1', 'line2', 'line3'}, set()

@pytest.fixture
def identical_sets():
    return {'line1', 'line2', 'line3'}, {'line1', 'line2', 'line3'}

@pytest.fixture
def different_sets():
    return {'line1', 'line2', 'line3'}, {'line2', 'line3', 'line4'}

def test_compare_cycle_empty_sets(empty_sets):
    text1, text2 = empty_sets
    same_text, diff_text = compare_cycle(text1, text2)
    assert same_text == []
    assert diff_text == []

def test_compare_cycle_one_empty_set(one_empty_set):
    text1, text2 = one_empty_set
    same_text, diff_text = compare_cycle(text1, text2)
    assert same_text == []
    assert sorted(diff_text) == ['line1', 'line2', 'line3']

def test_compare_cycle_identical_sets(identical_sets):
    text1, text2 = identical_sets
    same_text, diff_text = compare_cycle(text1, text2)
    assert sorted(same_text) == ['line1', 'line2', 'line3']
    assert diff_text == []

def test_compare_cycle_different_sets(different_sets):
    text1, text2 = different_sets
    same_text, diff_text = compare_cycle(text1, text2)
    assert sorted(same_text) == ['line2', 'line3']
    assert sorted(diff_text) == ['line1', 'line4']