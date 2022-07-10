# Given a long text as a string (let’s say the content of a book), find the most frequently occurring word in it.

# Example input:
# “The green label is green. The red label is not green.”

# Example output:
# “green”

def most_frequent_word(s: str) -> str:
    words = list()
    punctuation = {' ', '-', '.', ','}
    word = ''
    
    for c in s:
        if c not in punctuation:
            word += c
        elif len(word) > 0:
            words.append(word)
            word = ''
    
    if len(word) > 0:
        words.append(word)
    
    word_counts = dict()
    
    for w in words:
        word = w.lower()

        n = word_counts.get(word, 0)
        word_counts[word] = n + 1
            
    result = ''
    highest = 0
    
    for k, v in word_counts.items():
        if v > highest:
            result = k
            highest = v
        
    return result
