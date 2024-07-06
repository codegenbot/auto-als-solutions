```''
def parse_music(music_string: str) -> list:
    music_list = []
    i = 0
    while i < len(music_string):
        if music_string[i:i+2] == 'oO':
            music_list.append(4)
            i += 2
        elif music_string[i:i+3] == '.OO':
            music_list.append(1)
            i += 3
        elif music_string[i:i+5] == '..O.O':
            music_list.append(0.5)
            i += 4
    return music_list