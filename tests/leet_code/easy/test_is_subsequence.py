from algorithms.leet_code.easy.is_subsequence import is_subsequence

def test_is_subsequence():
    assert is_subsequence('ace', 'afdcfdfe')
    assert not is_subsequence('axc', 'ahbgdc')
    assert is_subsequence('asdf', 'asdfjkjkjkjk')
    assert is_subsequence('you', 'yewqweowereruwrwer')
    assert not is_subsequence('you', 'yewqweowererwrwer')
    assert not is_subsequence('you', 'ewqweowererwurwer')
    assert not is_subsequence('you', 'yo')
