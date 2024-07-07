def parse_music(music_string: str) -> List[int]:
    music_list = []
    for char in music_string:
        if char == 'o':
            if len(music_string) > i+1 and music_string[i+1] == '|':
                music_list.append(1)
                i += 2
            else:
                music_list.append(4)
                i += 1
        elif char == '.' and music_string[i:i+3] == '.|..|':
            music_list.append(8)
            i += 3
    return music_list