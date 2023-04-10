import pytest
from test_3 import sum_current_time

def test_must_be_valid_time():
    """tests an error is raised if the input is not in time format"""
    with pytest.raises(ValueError) as err:
        sum_current_time('55:06:33')

def test_output_is_int():
    """tests the output is an integer"""
    assert isinstance(sum_current_time('01:02:03'), int)

def test_output_is_correct():
    """tests the output is correct for different values"""
    assert sum_current_time('01:02:03') == 6
    assert sum_current_time('18:41:23') == 82
    assert sum_current_time('00:30:55') == 85


