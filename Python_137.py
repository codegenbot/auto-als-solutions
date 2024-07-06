```
def compare_one(a, b):
    if isinstance(a, str) and isinstance(b, (int, float)):
        return a if a.replace(",", ".").replace(".", ",").replace(" ", "") > str(b) else None
    elif isinstance(b, str) and isinstance(a, (int, float)):
        return b if b.replace(",", ".").replace(".", ",").replace(" ", "") > str(a) else None
    elif isinstance(a, str) and isinstance(b, str):
        return a if a.replace(",", ".").replace(".", ",").replace(" ", "") > b.replace(",", ".").replace(".", ",").replace(" ", "") else None
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return max(a, b) if a != b else None