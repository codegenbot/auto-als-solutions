def kebab_to_camel_case(s):
    def convert_to_camel_case(segment):
        parts = segment.split('-')
        return parts[0] + ''.join(word.capitalize() for word in parts[1:])
    
    return ' '.join(convert_to_camel_case(word) for word in s.split())

# Read input from user
input_string = input().strip()
print(kebab_to_camel_case(input_string))