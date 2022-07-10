from algorithms.interviews.arrays_and_strings.most_frequent_word import most_frequent_word

def test_most_frequent_word():
    assert most_frequent_word('The green label is green. The red label is not green.') == 'green'
    assert most_frequent_word('test') == 'test'
    assert most_frequent_word('My favorite color is blue-green. my friend\'s is green') == 'my'
    assert most_frequent_word('My favorite color is blue-green. my friend\'s is green. I don\'t like green.') == 'green'
    assert most_frequent_word('     test     ') == 'test'
    assert most_frequent_word('My favorite color is blue-green... my friend\'s is green. I don\'t like green.') == 'green'
