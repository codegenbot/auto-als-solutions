```
def camel_case(s):
    words = s.split("-")
    output = words[0].capitalize()
    for word in words[1:]:
        output += word.capitalize()
    return output