from algorithms.interviews.arrays_and_strings.group_anagrams import group_anagrams

def test_group_anagrams():
    assert group_anagrams(['eat','tea','tan','ate','nat','bat']) == [['eat','tea','ate'],['tan', 'nat'],['bat']]
