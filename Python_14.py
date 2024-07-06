from typing import List


def all_prefixes() -> List[str]:
    num_strings = int(input("Enter number of strings: "))
    string_list = []
    
    for _ in range(num_strings):
        new_string = input(f"Enter string {string_list.index(_)+1}: ")
        string_list.append(new_string)
        
    return [new_string[:i] for new_string in string_list for i in range(1, len(new_string) + 1)]


print(all_prefixes())