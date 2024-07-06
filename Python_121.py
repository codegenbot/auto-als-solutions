```
n = int(input())
def solution(lst):
    return sum(i for i in lst[1::2] if i % 2 != 0)
print(solution([i for i in range(1,n+1)]))