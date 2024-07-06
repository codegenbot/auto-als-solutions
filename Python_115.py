```
def max_fill(grid, capacity):
    total_water = 0
    for row in grid:
        stack = []
        j = len(row) - 1
        for i in range(len(row) - 1, -1, -1):
            if row[i] == 1:
                while stack and row[stack[-1]] != 1:
                    j = stack.pop()
                if not stack or row[j] == 0:
                    total_water += min(j + 1, i) - (j if j > i else j - len(row) + i)
                else:
                    total_water += stack[-1] - i
                stack.append(i)
            elif stack and row[stack[-1]] == 1:
                stack.pop()
        total_water = math.ceil(total_water / capacity)
    return total_water