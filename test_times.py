from times import time_range, compute_overlap_time
import pytest

in_and_out = [((time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)),
              [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]),
              ((time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00")), []),
              ((time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 30), time_range("2010-01-12 11:00:00", "2010-01-12 13:00:00", 2, 10)), [("2010-01-12 11:00:15", "2010-01-12 11:59:55")]),
              ((time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00") ), [])]


@pytest.mark.parametrize("test_input,expected", in_and_out)
def test_compute_overlap_time(test_input, expected):
    assert compute_overlap_time(*test_input) == expected


def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result==expected

def test_no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00")
    result = compute_overlap_time(large, short)
    expected = []
    assert result==expected

def test_mult_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 30)
    short = time_range("2010-01-12 11:00:00", "2010-01-12 13:00:00", 2, 10)
    result = compute_overlap_time(large, short)
    expected = [("2010-01-12 11:00:15", "2010-01-12 11:59:55")]
    assert result==expected

def test_edge_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00")
    result = compute_overlap_time(large, short)
    expected = []
    assert result==expected

def test_backwards_time_range():
    expected_error_message = "Backwards time range: endtime before starttime"
    with pytest.raises(ValueError, match=expected_error_message):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00", 1, 0)