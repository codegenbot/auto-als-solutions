def parse_music(music_string: str) -> List[int]:
    music_notes = {"o": 4, "o|": 2, ".|": 1}
    beats = []
    current_note = ""
    for char in music_string:
        if char == "o" or char == ".":
            current_note += char
        elif char == "|":
            if current_note in music_notes:
                beats.append(music_notes[current_note])
            current_note = ""
    if current_note in music_notes:
        beats.append(music_notes[current_note])
    return beats