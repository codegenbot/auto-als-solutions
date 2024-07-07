def parse_music(music_string: str) -> list:
    music_list = []
    notes = {'o': 4, 'o|': 2, '.||': 1}
    i = 0
    while i < len(music_string):
        if music_string[i:i+2] in notes:
            if music_string[i-1] == '.' and music_string[i:i+2] == 'o||':
                music_list.append(8)
            else:
                music_list.append(notes[music_string[i:i+2]])
            i += 2
        elif music_string[i] == 'o' and music_string[i+1] in ['o', '|']:
            music_list.append(4)
            i += 1
    return music_list