```Python
def sort_third(lst):
    return [i if isinstance(i, list) 
            else [] if i % 3 == 0 
            else [i] 
            for i in lst]