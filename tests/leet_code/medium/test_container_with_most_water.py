from algorithms.leet_code.medium.container_with_most_water import container_with_most_water

def test_container_with_most_water():
    assert container_with_most_water([1, 2, 3, 4, 5]) == 6
    assert container_with_most_water([1, 1]) == 1
    assert container_with_most_water([1, 3, 1, 3, 1]) == 6
    assert container_with_most_water([1, 1, 1, 1, 10, 10]) == 10
    assert container_with_most_water([10, 10, 1, 1, 1, 1]) == 10
