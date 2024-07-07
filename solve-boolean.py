def solveBoolean(input_str):
    if input_str == 'T':
        return True
    elif input_str == 'F':
        return False
    elif '&' in input_str and '|' in input_str:
        return ((input_str.split('&')[0] == 'T') and (input_str.split('|')[1] == 'T')) or ((input_str.split('&')[0] == 'F') and (input_str.split('|')[1] == 'F'))
    elif '&' in input_str:
        return input_str.split('&')[0] == 'T' and input_str.split('&')[1] == 'T'
    elif '|' in input_str:
        return input_str.split('|')[0] == 'T' or input_str.split('|')[1] == 'T'
    else:
        raise ValueError('Invalid expression')