# Given an array of strings, group the anagrams together. You can return the answer in any order.

def group_anagrams(words: list[str]) -> list[list[str]]:
    def get_key(word: str) -> str:
        A_CODE = ord('a')
        letters = [0] * 26

        for x in word:
            letters[ord(x) - A_CODE] += 1
        
        key = ''
        
        for i, x in enumerate(letters):
            key += chr(i + A_CODE) + str(x)
        
        return key
    
    word_groups = dict()

    if words:
        for x in words:
            key = get_key(x)
            group = word_groups.get(key, [])
            group.append(x)
            word_groups[key] = group
    else:
        return []
    
    return list(word_groups.values())
