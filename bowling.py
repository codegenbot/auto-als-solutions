```
def bowling_score(frames):
    score = 0
    current_frame_rolls = []
    
    frames = frames.replace('/', '')
    for char in frames:
        if char == 'X':
            score += 10
        elif char == '-':
            previous_frame_score = sum(current_frame_rolls)
            score += 10 + previous_frame_score
            current_frame_rolls = []
        else:
            current_frame_rolls.append(int(char))
    
    if len(current_frame_rolls) > 0:
        score += sum(current_frame_rolls)
    
    return score

frames = "7/3/5/5/10/0/1/7/6/4"
print(bowling_score(frames))