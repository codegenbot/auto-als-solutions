def parse_music(music_string: str) -> List[int]:
    notes = {"o": [4], "o|": [2, 4], ".|": [1, 2]}
    result = []
    i = 0
    while i < len(music_string):
        if music_string[i] == ".":
            i += 1
        note = ""
        while i < len(music_string) and (music_string[i] in "o|."):
            note += music_string[i]
            i += 1
        if "|" not in note:
            result.append(notes[note][0])
        else:
            for value in notes[note]:
                result.append(value)
    return result