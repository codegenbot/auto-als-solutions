```
def parse_music(music_string: str) -> List[int]:
    result = []
    i = 0
    while i < len(music_string):
        if music_string[i] == 'o':
            note_length = 4
        elif music_string[i:i+2] == 'o|':
            note_length = 2
        elif music_string[i:i+3] == '.|..':
            note_length = 1
        i += note_length
        result.append(note_length)
    return result