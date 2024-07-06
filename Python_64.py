```
def vowels_count(s):
    s = s.lower()
    count = 0
    for char in s:
        if char.isalpha():
            if char in 'aeiouy' and (char == 'y' or not s.index(char) == len(s)-1):
                count += 1
    return count