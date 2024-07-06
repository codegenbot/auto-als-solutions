from typing import List


def parse_music(music_string: str) -> List[int]:
    notes = {"o": 4, "o|": 2, ".|": 1}
    beats = []
    i = 0
    while i < len(music_string):
        if music_string[i] == "." and music_string[i + 1] == "|":
            i += 1
        beat_length = notes[music_string[i : i + 2]]
        beats.append(beat_length)
        i += 2
    return beats