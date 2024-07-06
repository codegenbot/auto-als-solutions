```
def check_dict_case(dict):
    if len(dict) == 0:
        return False
    for key in dict:
        if not (key.islower() or key.isupper()):
            return False
    return True