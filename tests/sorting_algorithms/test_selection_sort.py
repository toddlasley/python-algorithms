from algorithms.sorting_algorithms.selection_sort import selection_sort

def test_selection_sort():
    assert selection_sort([0, 1, 2, 3]) == [0, 1, 2, 3]
    assert selection_sort([1, 0, 3, 2]) == [0, 1, 2, 3]
    assert selection_sort([3, 2, 1, 0]) == [0, 1, 2, 3]
    assert selection_sort([ 2, 3, 4, 6, 5, 1, 0]) == [0, 1, 2, 3, 4, 5, 6]
    