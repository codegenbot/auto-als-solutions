```
def check_dict_case(dict):
    if len(dict) == 0:
        return False
    keys = [key for key in dict]
    all_lower = all(key.islower() for key in keys)
    all_upper = all(key.isupper() for key in keys)
    return all_lower or all_upper