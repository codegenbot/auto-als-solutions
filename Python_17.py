```
def parse_music(input_string):
    note = ""
    if "o|" in input_string:
        note += "1"
    elif ".":
        note += "0"
    output = []
    i = 0
    while i < len(input_string):
        if input_string[i] == "o":
            j = i + 3
            while i < j and i < len(input_string) - 1 and input_string[i+1] != "|":
                i += 1
            note_length = int(input_string[i+1])
            for _ in range(note_length):
                if input_string[j] == "o":
                    output.append(2)
                elif input_string[j] == ".":
                    output.append(1)
                j += 1
        elif input_string[i] == ".":
            output.append(0)
        i += 1
    return [int(i) for i in note.split()]