from algorithms.leet_code.medium.longest_palindromic_substring import Solution

def test_longest_palindromic_substring():
    assert Solution.longest_palindromic_substring('babad') == 'bab' or Solution.longest_palindromic_substring('babad') == 'aba'
    assert Solution.longest_palindromic_substring('asdf32123poiu') == '32123'
    assert Solution.longest_palindromic_substring('jfdfimvieracecar') == 'racecar'
    assert Solution.longest_palindromic_substring('aaaaaaa123') == 'aaaaaaa'
    assert Solution.longest_palindromic_substring('123aaaaa987') == 'aaaaa'
    assert Solution.longest_palindromic_substring('9876543aaa') == 'aaa'
    assert Solution.longest_palindromic_substring('bb123') == 'bb'
    assert Solution.longest_palindromic_substring('123bb987') == 'bb'
    assert Solution.longest_palindromic_substring('9876543bbbb') == 'bbbb'
