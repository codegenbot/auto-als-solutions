```
def file_name_check(file_name):
    count = sum(c.isdigit() for c in file_name)
    if count > 3:
        return 'No'
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    first, second = parts
    if not first[0].isalpha():
        return 'No'
    if set(second) != {'txt', 'exe', 'dll'}:
        return 'No'
    return 'Yes'