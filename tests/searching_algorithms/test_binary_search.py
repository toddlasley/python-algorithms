from algorithms.searching_algorithms.binary_search import binary_search

def test_binary_search():
    assert binary_search([0, 1, 2, 3], 0) == 0
    assert binary_search([0, 1, 2, 3], 1) == 1
    assert binary_search([0, 1, 2, 3], 2) == 2
    assert binary_search([0, 1, 2, 3], 3) == 3
    assert binary_search([0, 1, 2, 3], 4) == -1
    assert binary_search([0, 1, 2, 3, 4, 5, 6], 0) == 0
    assert binary_search([0, 1, 2, 3, 4, 5, 6], 1) == 1
    assert binary_search([0, 1, 2, 3, 4, 5, 6], 3) == 3
    assert binary_search([0, 1, 2, 3, 4, 5, 6], 5) == 5
    assert binary_search([0, 1, 2, 3, 4, 5, 6], 6) == 6
    assert binary_search([0, 1, 2, 3, 4, 5, 6], 7) == -1
