```
from typing import List


def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    note_type = ''
    
    for char in music_string:
        if char not in ['o', 'o|', '.', '|']:
            continue
        if char != note_type[0]:
            result.append(notes[note_type])
            note_type = char + (note_type[1] if note_type else '|')
        else:
            note_type += char
    
    result.append(notes[note_type])
    
    return result