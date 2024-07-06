```python
def parse_music(music_string: str) -> List[int]:
    notes = {'o': [4], 'o|': [2, 0], '.|': [1, 0]}
    result = []
    i = 0
    while i < len(music_string):
        if music_string[i] == '.':
            i += 1
        note = ''
        while i < len(music_string) and (music_string[i] in 'o|.' or music_string[i] == '|'):
            note += music_string[i]
            i += 1
        durations = notes[note]
        for duration in durations:
            result.append(duration)
    return result