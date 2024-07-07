```python
def basement(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
        if total < 0:
            return i+1

print(basement([1])) # 0
print(basement([-100, 1])) # 0
print(basement([2, -1, 100])) # 0
print(basement([2, -95, 100])) # 0
print(basement([2, -30, 5])) # 0