def bowling_score(bowls):
    score = 0
    i = 0
    for frame in range(10):
        if bowls[i] == 'X':  # Strike
            score += 10 + (10 if bowls[i+1] == 'X' else (10 if bowls[i+1] == '/' else (0 if bowls[i+1] == '-' else int(bowls[i+1])))) + (10 if bowls[i+2] == 'X' else (10 if bowls[i+2] == '/' else (0 if bowls[i+2] == '-' else int(bowls[i+2]))))
            i += 1
        elif bowls[i+1] == '/':  # Spare
            score += 10 + (10 if bowls[i+2] == 'X' else (0 if bowls[i+2] == '-' else int(bowls[i+2])))
            i += 2
        else:  # Open frame
            score += (0 if bowls[i] == '-' else int(bowls[i])) + (0 if bowls[i+1] == '-' else int(bowls[i+1]))
            i += 2
    return score

# Read input
input_str = input().strip()
print(bowling_score(input_str))