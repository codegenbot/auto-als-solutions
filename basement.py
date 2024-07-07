Here's the solution:

def basement(input_list):
    total = 0
    for i, num in enumerate(input_list):
        total += num
        if total < 0:
            return i
    return -1