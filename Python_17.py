```
def parse_music(music_string: str) -> list[int]:
    music_notes = ["o", "o|", ".|"]
    beats_per_note = [4, 2, 1]
    result = []

    for note in music_string.split():
        if note in music_notes:
            result.append(beats_per_note[music_notes.index(note)])

    return result