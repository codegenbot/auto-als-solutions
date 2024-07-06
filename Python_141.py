```
def file_name_check(file_name):
    if len(file_name.split('.')) != 2:
        return 'No'
    before_dot = file_name.split('.')[0]
    after_dot = file_name.split('.')[1].lower()
    if not before_dot[0].isalpha():
        return 'No'
    if not (after_dot in ['txt', 'exe', 'dll']):
        return 'No'
    digits_count = sum(c.isdigit() for c in file_name)
    if digits_count > 3:
        return 'No'
    return 'Yes'