from algorithms.leet_code.medium.spiral_matrix import spiral_traversal

def test_spiral_matrix():
    assert spiral_traversal([[0, 1], [2, 3]]) == [0, 1, 3, 2]
    assert spiral_traversal([[0, 1, 2], [3, 4, 5], [6, 7, 8]]) == [0, 1, 2, 5, 8, 7, 6, 3, 4]
    assert spiral_traversal([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]) == [0, 1, 2, 5, 8, 11, 10, 9, 6, 3, 4, 7]
    assert spiral_traversal([[0, 1, 2, 9], [3, 4, 5, 10], [6, 7, 8, 11]]) == [0, 1, 2, 9, 10, 11, 8, 7, 6, 3, 4, 5]
    assert spiral_traversal([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]) == [5, 1, 9, 11, 10, 7, 16, 12, 14, 15, 13, 2, 4, 8, 6, 3]
