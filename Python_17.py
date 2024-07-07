```
def parse_music(music_string: str) -> list:
    notes = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11, 'o': 4}
    music_list = []
    i = 0
    while i < len(music_string):
        if music_string[i] == '.':
            note_duration = 1
        elif music_string[i:i+2] in ['o|', '||']:
            if music_string[i:i+2] == 'o|':
                note_duration = 4
            else:
                note_duration = 1
            i += 2
        if i < len(music_string):
            if music_string[i] not in 'o.|':
                return ['Invalid input']
            note_name = music_string[i]
            if note_name in notes:
                music_list.append((notes[note_name], note_duration))
                i += 1
    return music_list