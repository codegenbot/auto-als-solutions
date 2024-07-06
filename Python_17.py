def parse_music(music_string: str) -> List[int]:
    notes = {"o": [4], "o|": [2, 1], ".|": [1]}
    result = []
    i = 0
    while i < len(music_string):
        note = ""
        while i < len(music_string) and (
            music_string[i] in "o.|" or music_string[i] == "|"
        ):
            if music_string[i] == ".":
                break
            note += music_string[i]
            i += 1
        if note in notes:
            result.extend(notes[note])
    return result