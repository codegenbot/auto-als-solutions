def parse_music(user_input=""):
    note = input("Enter the music string (o| followed by digit for note duration, .|| for 1 beat): ")
    return [int(x) if x.isdigit() else 1 for x in note.replace('.|', '1').replace('o|', user_input)]