```
def even_odd_count(num):
    num = abs(num)
    count_even = sum(1 for i in str(num) if int(i) % 2 == 0)
    count_odd = len(str(num)) - count_even
    return (count_even, count_odd)