from algorithms.leet_code.medium.three_sum_zero import three_sum_zero

def test_three_sum_zero():
    assert three_sum_zero([-1, -1, 0, 2]) == [[-1, -1, 2]]
    assert three_sum_zero([-2, 0, 2, -1, -1, 0, 5]) == [[-2, 0, 2], [-1, -1, 2]]
    assert three_sum_zero([]) == []
    assert three_sum_zero([1, 2, 3]) == []
    assert three_sum_zero([-1, -1, -1, -1, -1, 0, -1, 1, 1, 1, 1, 1]) == [[-1, 0, 1]]
