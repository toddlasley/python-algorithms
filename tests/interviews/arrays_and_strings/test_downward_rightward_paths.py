from algorithms.interviews.arrays_and_strings.downward_rightward_paths import downward_rightward_paths

def test_downward_rightward_paths():
    assert downward_rightward_paths([[0, 0]] * 2) == 2
    assert downward_rightward_paths([[0, 0]] * 3) == 3
    assert downward_rightward_paths([[0, 0, 0]] * 2) == 3
    assert downward_rightward_paths([[0, 0, 0]] * 3) == 6
