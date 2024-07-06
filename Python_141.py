```
def file_name_check(file_name):
    if len([i for i in set(file_name) if i.isdigit()]) > 3:
        return 'No'
    if '.' not in file_name or file_name.split('.')[0].strip().isalpha() == False:
        return 'No'
    if file_name.split('.')[1].lower() not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'