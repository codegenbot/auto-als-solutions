```
def parse_music(music_string: str) -> list:
    music_list = []
    i = 0
    while i < len(music_string):
        if i < len(music_string) - 1 and music_string[i:i+2] == 'o|':
            note_duration = int(music_string[i-1]) * 4 if music_string[i-1].isdigit() else 4
            music_list.append(note_duration)
            i += 2
        elif music_string[i:i+3] == '.||':
            music_list.append(1)
            i += 3
    return music_list