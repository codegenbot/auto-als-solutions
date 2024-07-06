````
def total_match(lst1, lst2):
    if len([s for s in lst1 if s in lst2]) > len([s for s in lst2 if s in lst1]):
        return lst1
    elif len([s for s in lst1 if s in lst2]) < len([s for s in lst2 if s in lst1]):
        return lst2
    else:
        return lst1