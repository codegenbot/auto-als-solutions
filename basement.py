```
basement = lambda arr: next((i for i in range(len(arr)) if sum(arr[:i+1]) < 0), None)
print(basement([1])) 
print(basement([-100, 1])) 
print(basement([2, -1, 100])) 
print(basement([2, -95, 100])) 
print(basement([2, -30, 5]))