Here is the task description:

Write a Python function called `file_name_check` that takes a file name as input and returns 'Yes' if the file name meets certain criteria, otherwise it should return 'No'. The criteria are:
- The file name must not contain more than three digits.
- The file name must have exactly one dot (.) character.
- The part of the file name before the dot must consist only of letters.
- The extension after the dot must be either 'txt', 'exe', or 'dll'.

Here is the corrected code:

```
def file_name_check(file_name):
    if len([c for c in file_name if c.isdigit()]) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    dot_index = file_name.index('.')
    if not file_name[:dot_index].isalpha():
        return 'No'
    extension = file_name[dot_index + 1:]
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'