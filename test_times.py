from times import time_range, compute_overlap_time
import pytest
import yaml


def test_backwards_time_range():
    expected_error_message = "Backwards time range: endtime before starttime"
    with pytest.raises(ValueError, match=expected_error_message):
        time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00", 1, 0)


with open("fixtures.yaml", "r") as f:
    test_cases = yaml.safe_load(f)

test_data = []
for case in test_cases:
    case_name = list(case.keys())[0]
    case_value = case[case_name]
    
    time_input_1 = case_value['time_range_1']
    time_1 = time_range(time_input_1['start'], time_input_1['end'], time_input_1['n_intervals'], time_input_1['interval_gap'])
    time_input_2 = case_value['time_range_2']
    time_2 = time_range(time_input_2['start'], time_input_2['end'], time_input_2['n_intervals'], time_input_2['interval_gap'])
    print(case_value['expected'])
    expected = [eval(x) for x in case_value['expected']]
    
    test_data.append(([time_1, time_2], expected))

@pytest.mark.parametrize("test_input, expected", test_data)
def test_compute_overlap_time(test_input, expected):
    assert compute_overlap_time(*test_input) == expected