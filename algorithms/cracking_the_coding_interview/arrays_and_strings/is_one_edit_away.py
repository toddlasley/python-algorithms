# 1.5: Given two strings, write a function to check if they are
# one (or zero) edit away.

# Solution: p. 199

def is_one_edit_away(s: str, t: str) -> bool:
    if len(s) - len(t) > 1:
        return False
    
    difference_found = False
    longer: str
    shorter: str

    if len(s) > len(t):
        longer = s
        shorter = t
    else:
        longer = t
        shorter = s
    
    longer_i = shorter_i = 0

    while shorter_i < len(shorter) and longer_i < len(longer):
        if shorter[shorter_i] != longer[longer_i]:
            if difference_found:
                return False
            else:
                difference_found = True
            
            if len(s) == len(t):
                shorter_i = shorter_i + 1
        else:
            shorter_i = shorter_i + 1
        
        longer_i = longer_i + 1

    return True
