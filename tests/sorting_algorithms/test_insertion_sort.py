from algorithms.sorting_algorithms.insertion_sort import insertion_sort

def test_insertion_sort():
    assert insertion_sort([0, 1, 2, 3]) == [0, 1, 2, 3]
    assert insertion_sort([1, 0, 3, 2]) == [0, 1, 2, 3]
    assert insertion_sort([3, 2, 1, 0]) == [0, 1, 2, 3]
    assert insertion_sort([ 2, 3, 4, 6, 5, 1, 0]) == [0, 1, 2, 3, 4, 5, 6]
    