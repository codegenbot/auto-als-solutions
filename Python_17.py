```
def parse_music(music_string: str) -> list:
    """Returns a list of note durations from a given music string.
    
    A duration is represented by one character ('o') for quarter note,
    'o|' for eighth note and '.|' for sixteenth note.
    
    Parameters:
    music_string (str): The input string representing the music notation.
    
    Returns:
    list: A list of integers, where each integer represents a note duration in seconds.
    """
    music_list = []
    i = 0
    while i < len(music_string):
        if music_string[i] == 'o':
            music_list.append(4)
            i += 1
        elif music_string[i:i+2] == 'o|':
            music_list.append(2)
            i += 2
        elif music_string[i:i+3] == '.|':
            music_list.append(1)
            i += 3
    return music_list