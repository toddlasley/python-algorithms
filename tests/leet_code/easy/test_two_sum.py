from algorithms.leet_code.easy.two_sum import *

def test_two_sum():
    assert two_sum([1, 2, 3, 4], 3) == [0, 1]
    assert two_sum([4, 3, 2, 1], 3) == [2, 3]
    assert two_sum([2, 3, 4, 1], 3) == [0, 3]
    assert two_sum([3, 1, 2, 4], 3) == [1, 2]