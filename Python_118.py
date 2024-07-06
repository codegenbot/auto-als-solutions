```
def get_closest_vowel(word):
    word = word[::-1]  # Reverse the string
    result = ''
    for char in word:
        if char.lower() in 'aeiou':  # Check if character is a vowel
            return char.lower()[::-1]  # Return the reversed vowel
    return ''