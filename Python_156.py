```
def int_to_mini_roman(number):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    mini_roman = ''
    for i in range(3999):  # iterate through all possible roman numerals
        if i >= number:
            break
        roman_str = ''
        while i > 0:
            for key, value in roman.items():
                if i >= value:
                    roman_str += key
                    i -= value
                elif i < value and i >= value / 10:
                    roman_str += key * (value // 10)
                    i -= value // 10
                    break
        mini_roman = roman_str.lower()
    return mini_roman[:len(str(number))].ljust(len(mini_roman), 'i')