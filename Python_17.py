Here is the solution:

```
from typing import List


def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    temp = ''
    for char in music_string:
        if char not in notes:
            continue
        temp += char
        if len(temp) > 1 or (len(temp) == 1 and temp != 'o'):
            result.append(notes[temp])
            temp = ''
    return result