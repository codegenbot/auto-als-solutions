```
def parse_music(music_string: str) -> List[int]:
    result = []
    i = 0
    while i < len(music_string):
        if music_string[i:i+2] == 'o|':
            result.append(2)
            i += 2
        elif music_string[i:i+3] == '.|.':
            result.append(1)
            i += 3
        elif music_string[i] == 'o':
            note_length = 4
            while i < len(music_string) and music_string[i] != '|':
                i += 1
            if i < len(music_string):
                if music_string[i:i+2] == 'o|':
                    note_length = 2
                elif music_string[i:i+3] == '.|.':
                    note_length = 1
                result.append(note_length)
        i += 1
    return result