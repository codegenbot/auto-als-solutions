def camel_case(s): 
    words = s.split('-') 
    return ''.join(word.capitalize() if i > 0 else word.title() for i,word in enumerate(words))