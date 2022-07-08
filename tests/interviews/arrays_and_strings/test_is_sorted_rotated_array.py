from algorithms.interviews.arrays_and_strings.is_sorted_rotated_array import is_sorted_rotated_array

def test_is_sorted_rotated_array():
    assert is_sorted_rotated_array([3, 4, 5, 1, 2])
    assert not is_sorted_rotated_array([3, 4, 5, 1, 2, 0])
    assert not is_sorted_rotated_array([7, 9, 11, 12])
    assert is_sorted_rotated_array([7, 9, 11, 12, 5])
    assert not is_sorted_rotated_array([7, 9, 11, 100, 12, 5])
    assert not is_sorted_rotated_array([3, 4, 5, 1, 2, 7])
