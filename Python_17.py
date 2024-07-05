Here is the complete problem:

**Problem:** Write a Python function that takes as input a string representing musical notes in the following format: "o" for whole note, "o|" for half note, and ".| " for quarter note. The function should return a list of integers where each integer represents the duration (4 beats for a whole note, 2 beats for a half note, and 1 beat for a quarter note).

**Function Signature:**
```
def parse_music(music_string: str) -> List[int]:
    ...
```

Here is my code:
```
from typing import List


def parse_music(music_string: str) -> List[int]:
    result = []
    i = 0
    while i < len(music_string):
        if music_string[i] == 'o':
            result.append(4)
            i += 1
        elif music_string[i:i+2] == 'o|':
            result.append(2)
            i += 2
        elif music_string[i:i+3] == '.| ':
            result.append(1)
            i += 3
    return result