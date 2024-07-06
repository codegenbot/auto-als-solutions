def fruit_distribution(s, n):
    s = s.replace("apples and ", "")
    s = s.replace(" oranges", "")
    n = int(n)
    parts = s.split(" ")
    
    if len(parts) >= 2:
        return n - (int(parts[0].replace(" apples", "")) + int(parts[-1]))
    else:
        return 0