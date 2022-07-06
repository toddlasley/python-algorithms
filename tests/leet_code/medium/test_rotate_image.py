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

    c = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    c_expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    rotate_image(c)
    assert c == c_expected
