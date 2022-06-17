from algorithms.leet_code.medium.rotate_image import rotate_image

def test_rotate_image():
    a = [[0, 1], [2, 3]]
    a_expected = [[2, 0], [3, 1]]
    rotate_image(a)
    assert a == a_expected

    b = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    b_expected = [[6, 3, 0], [7, 4, 1], [8, 5, 2]]
    rotate_image(b)
    assert b == b_expected
