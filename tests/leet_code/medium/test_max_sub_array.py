from algorithms.leet_code.medium.max_sub_array import max_sub_array

def test_max_sub_array():
    assert max_sub_array([1, 2, 3, 4]) == 10
    assert max_sub_array([1]) == 1
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sub_array([5,4,-1,7,8]) == 23
    assert max_sub_array([-2, -2, 5]) == 5
    assert max_sub_array([1,2,-1,-2,2,1,-2,1,4,-5,4]) == 6
