def total_match(lst1, lst2):
    sum1 = sum(len(s) for s in lst1)
    sum2 = sum(len(s) for s in lst2)

    if sum1 < sum2:
        print("List1 has a shorter total length")
        return lst1
    elif sum1 > sum2:
        print("List2 has a longer total length")
        return lst2
    else:
        print("Lists have the same total length")
        return lst1