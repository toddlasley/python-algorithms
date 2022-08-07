from algorithms.interviews.math.fibonacci import fibonacci_iterative, fibonacci_recursive

# 0 1 1 2 3 5 8 13 21 34
def test_fibonacci():
    assert fibonacci_recursive(0) == fibonacci_iterative(0) == 0
    assert fibonacci_recursive(1) == fibonacci_iterative(1) == 1
    assert fibonacci_recursive(2) == fibonacci_iterative(2) == 1
    assert fibonacci_recursive(3) == fibonacci_iterative(3) == 2
    assert fibonacci_recursive(4) == fibonacci_iterative(4) == 3
    assert fibonacci_recursive(5) == fibonacci_iterative(5) == 5
    assert fibonacci_recursive(6) == fibonacci_iterative(6) == 8
    assert fibonacci_recursive(7) == fibonacci_iterative(7) == 13
    assert fibonacci_recursive(8) == fibonacci_iterative(8) == 21
    assert fibonacci_recursive(9) == fibonacci_iterative(9) == 34
