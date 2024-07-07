Here is the completed code:

def cut_vector(vector):
    left = 0
    for i in range(len(vector) - 1):
        if abs(sum(vector[:i+1]) - sum(vector[i:])) <= abs(sum(vector[:left+1]) - sum(vector[left:])):
            left = i
    return vector[:left+1], vector[left:]