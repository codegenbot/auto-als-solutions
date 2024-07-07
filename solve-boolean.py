def solveBoolean(expression):
    def evaluate(expression):
        while "|" in expression:
            left, right = expression.split("|", 1)
            if "&" in left and "&" in right:
                return str(
                    (
                        left[: left.index("&")] + "T"
                        if left[: left.index("&")] == "f&"
                        else "F"
                    )
                    or (
                        right[: right.index("&")] + "T"
                        if right[: right.index("&")] == "f&"
                        else "F"
                    )
                )
            elif "&" in left:
                return "T" if evaluate(left) == "True" else "F"
            elif "&" in right:
                return "F" if evaluate(right) == "True" else "T"
            else:
                expression = (
                    evaluate(left[: left.index("&")]) + "T"
                    if left[: left.index("&")] == "f&"
                    else "F"
                ) or (
                    evaluate(right[: right.index("&")]) + "T"
                    if right[: right.index("&")] == "f&"
                    else "F"
                )
        while "&" in expression:
            left, right = expression.split("&", 1)
            if "|" in left and "|" in right:
                return str(
                    (
                        left[: left.index("|")] + "T"
                        if left[: left.index("|")] == "t|"
                        else "F"
                    )
                    or (
                        right[: right.index("|")] + "T"
                        if right[: right.index("|")] == "f|"
                        else "F"
                    )
                )
            elif "|" in left:
                return "T" if evaluate(left) == "True" else "F"
            elif "|" in right:
                return "F" if evaluate(right) == "True" else "T"
            else:
                expression = (
                    evaluate(left[: left.index("|")]) + "T"
                    if left[: left.index("|")] == "t|"
                    else "F"
                ) or (
                    evaluate(right[: right.index("|")]) + "T"
                    if right[: right.index("|")] == "f|"
                    else "F"
                )
        return str(expression == "t")

    return evaluate(expression)