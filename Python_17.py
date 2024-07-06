from typing import List


def parse_music(music_string: str) -> List[int]:
    notes = {"o": 4, "o|": 2, ".|": 1}
    result = []
    i = 0
    while i < len(music_string):
        if music_string[i] == ".":
            j = i + 1
            while j < len(music_string) and music_string[j] != "|":
                j += 1
            result.append(notes[music_string[i:j]])
            i = j
        else:
            result.append(notes[music_string[i : i + 2]])
            i += 2
    return result