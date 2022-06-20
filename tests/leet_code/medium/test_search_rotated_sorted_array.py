from algorithms.leet_code.medium.search_rotated_sorted_array import search_rotated_sorted_array

def test_search_rotated_sorted_array() -> int:
    assert search_rotated_sorted_array([4, 5, 6, 1, 2, 3], 1) == 3
    assert search_rotated_sorted_array([4, 5, 6, 1, 2, 3], 2) == 4
    assert search_rotated_sorted_array([4, 5, 6, 1, 2, 3], 4) == 0
    assert search_rotated_sorted_array([4, 5, 6, 1, 2, 3], 3) == 5
    assert search_rotated_sorted_array([4, 5, 6, 1, 2, 3], 7) == -1
    assert search_rotated_sorted_array([6, 1, 2, 3, 4, 5], 1) == 1
    assert search_rotated_sorted_array([6, 1, 2, 3, 4, 5], 6) == 0
    assert search_rotated_sorted_array([6, 1, 2, 3, 4, 5], 5) == 5
    assert search_rotated_sorted_array([6, 1, 2, 3, 4, 5], 1) == 1
    assert search_rotated_sorted_array([6, 1, 2, 3, 4, 5], 7) == -1
    assert search_rotated_sorted_array([1, 2, 3, 4, 5, 6], 1) == 0
    assert search_rotated_sorted_array([1, 2, 3, 4, 5, 6], 3) == 2
    assert search_rotated_sorted_array([1, 2, 3, 4, 5, 6], 6) == 5
    assert search_rotated_sorted_array([1, 2, 3, 4, 5, 6], 7) == -1
