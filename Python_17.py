```
def parse_music(music_string: str) -> list:
    notes = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
    music_list = []
    i = 0
    while i < len(music_string):
        if i+3 <= len(music_string) and music_string[i:i+3] == '.||':
            note_duration = 1
            i += 3
        elif i+2 <= len(music_string) and music_string[i:i+2] in ['o|', 'O|']:
            note_duration = 4
            i += 2
        else:
            i += 1
        if i < len(music_string) and music_string[i] in notes:
            music_list.append((notes[music_string[i]], note_duration))
    return music_list