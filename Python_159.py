```
def eat(hungry, needed, remaining):
    if hungry < needed:
        return ["Hungry", "Not enough food"]
    elif needed > remaining:
        return ["Full", "Too much food"]
    else:
        eaten = min(needed, remaining)
        leftover = needed - eaten
        if leftover == 0:
            return [str(eaten), "Full"]
        elif eaten < needed and hungry > remaining:
            return ["Not full", str(leftover)]
        else:
            return [str(eaten), "Hungry"]