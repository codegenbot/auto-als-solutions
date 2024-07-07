```
print(sum(i for i in range(len([1])))) # 0
print(sum(i for i in range(len([-100, 1])))) # 0
print(sum(i for i in range(len([2, -1, 100])))) # 0
print(sum(i for i in range(len([2, -95, 100])))) # 0
print(sum(i for i in range(len([2, -30, 5])))) # 0