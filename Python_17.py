from typing import List


def parse_music(music_string: str) -> List[int]:
    music_list = []
    note_length = 0
    for char in music_string:
        if char == "o":
            note_length += 4
        elif char == "|":
            note_length = max(note_length - 2, 1)
        elif char == ".":
            note_length -= 1
            if note_length < 1:
                note_length = 1
        music_list.append(note_length)
    return music_list