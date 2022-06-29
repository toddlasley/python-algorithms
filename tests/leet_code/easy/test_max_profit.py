from algorithms.leet_code.easy.max_profit import max_profit

def test_max_profit():
    assert max_profit([1, 2]) == 1
    assert max_profit([1, 2, 3])  == 2
    assert max_profit([2, 4, 5, 1, 2, 7]) == 6
    assert max_profit([2, 4, 5, 3, 4, 7]) == 5
    assert max_profit([2, 1]) == 0
    assert max_profit([2, 2]) == 0
    assert max_profit([4, 3, 2, 1]) == 0
