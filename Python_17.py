Here is the modified code:

Task: Write a function that parses a string representing musical notes and returns a list of integers where each integer represents the duration of the note.

def parse_music(music_string: str) -> List[int]:
    result = []
    i = 0
    while i < len(music_string):
        if music_string[i] == 'o':
            result.append(4)
            i += 1
        elif music_string[i:i+2] == 'o|':
            result.append(2)
            i += 2
        elif music_string[i:i+3] == '.| ':
            result.append(1)
            i += 3
    return result