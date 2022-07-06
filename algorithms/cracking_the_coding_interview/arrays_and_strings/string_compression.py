# 1.6: Implement a method to perform basic string compression using the counts of
# repeated characters. If the compressed string would not become smaller than the
# original string, your method should return the original string.

# Solution: p. 201 (identify compressed string length before building to be more space efficient)

def compress_string(s: str) -> str:
    if len(s) > 0:
        compressed = s[0]
        n = 1
        
        for x in s[1:]:
            if x != compressed[-1]:
                compressed += str(n) + x
                n = 1
            else:
                n += 1
        
        compressed += str(n)

        return s if len(s) <= len(compressed) else compressed
    else:
        return s
