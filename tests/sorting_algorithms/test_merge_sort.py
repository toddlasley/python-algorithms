from algorithms.sorting_algorithms.merge_sort import MergeSort

def test_merge_sort():
    assert MergeSort.sort([0, 1, 2, 3]) == [0, 1, 2, 3]
    assert MergeSort.sort([1, 0, 3, 2]) == [0, 1, 2, 3]
    assert MergeSort.sort([3, 2, 1, 0]) == [0, 1, 2, 3]
    assert MergeSort.sort([ 2, 3, 4, 6, 5, 1, 0]) == [0, 1, 2, 3, 4, 5, 6]
    