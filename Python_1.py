```
while stack and stack[-1] == "(":
    stack.pop()
if current_group:
    groups.append("(" + current_group + ")")
return [g for g in groups if g]