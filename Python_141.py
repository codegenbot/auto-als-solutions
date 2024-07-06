```
def file_name_check(file_name):
    if len([c for c in file_name if c.isdigit()]) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    prefix, suffix = file_name.rsplit('.', 1)
    if not prefix[0].isalpha():
        return 'No'
    extensions = ['txt', 'exe', 'dll']
    if suffix.lower() not in extensions:
        return 'No'
    return 'Yes'