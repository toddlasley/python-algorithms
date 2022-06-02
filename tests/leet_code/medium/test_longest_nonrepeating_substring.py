from algorithms.leet_code.medium.longest_nonrepeating_substring import longest_nonrepeating_substring

def test_longest_nonrepeating_substring():
    assert longest_nonrepeating_substring('') == 0
    assert longest_nonrepeating_substring('a') == 1
    assert longest_nonrepeating_substring('blah') == 4
    assert longest_nonrepeating_substring('1asdffffasd') == 5
    assert longest_nonrepeating_substring('ffffffas') == 3
    assert longest_nonrepeating_substring('aaaaaa') == 1
    assert longest_nonrepeating_substring('dvdf') == 3
    assert longest_nonrepeating_substring('pwwkew') == 3
