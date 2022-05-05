import pytest

@pytest.fixture
def empty_list():
    return []

@pytest.fixture
def string_value():
    return "hello"

def test_len_of_empty_list(empty_list, string_value):
    assert isinstance(empty_list, list)
    assert len(empty_list) == 0