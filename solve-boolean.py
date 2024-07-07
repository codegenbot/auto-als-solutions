def solveBoolean(input_str):
    if input_str == "T":
        return True
    elif input_str == "F":
        return False
    elif "&" in input_str:
        res = [solveBoolean(part) for part in input_str.split("&")]
        return all(res)
    elif "|" in input_str:
        res = [solveBoolean(part) for part in input_str.split("|")]
        return any(res)