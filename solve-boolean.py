def solve_boolean(expression):
    if expression == "T":
        return True
    elif expression == "F":
        return False
    else:
        stack = [expression]
        while stack:
            s = stack.pop()
            if "&" in s:
                a, b = s.split("&")
                stack.append(b)
                yield not (yield from solve_boolean(a))
            elif "|" in s:
                a, b = s.split("|")
                stack.extend([a, b])
                yield (yield from solve_boolean(a)) or (yield from solve_boolean(b))