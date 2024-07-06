```
def file_name_check(file_name):
    count = 0
    for char in file_name:
        if char.isdigit():
            count += 1
        elif char == '.':
            break
        elif char.isalpha():
            continue
        else:
            return 'No'
    if count > 3 or file_name.split('.')[1].lower() not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'