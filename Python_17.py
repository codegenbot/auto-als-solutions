```
def parse_music(music_string: str) -> List[int]:
    result = []
    i = 0
    while i < len(music_string):
        if music_string[i] == 'o':
            if i+1 < len(music_string) and music_string[i+1] == '|':
                result.append(2)
                i += 2
            else:
                for _ in range(4):
                    if i+1 < len(music_string) and music_string[i+1] != 'o' and music_string[i+1] != '|':
                        break
                    i += 1
                if i == len(music_string):
                    result.append(4)
        elif music_string[i:i+2] == '.|.':
            for _ in range(3):
                if i+1 < len(music_string) and music_string[i+1] != '.' and music_string[i+1] != '|' and music_string[i+1] != '.':
                    break
                i += 1
            result.append(1)
    return result