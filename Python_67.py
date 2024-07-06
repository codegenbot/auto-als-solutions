```
def fruit_distribution(s,n):
    s = s.replace('apples and', 'apples ').replace('oranges and', 'oranges ')
    words = s.split()
    return n - int(words[words.index('apples')+1].replace('apples', '')) - int(words[words.index('oranges')+1].replace('oranges', ''))