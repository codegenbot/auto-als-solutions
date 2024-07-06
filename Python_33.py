def 'sort_third'(lst): 
    sorted_lst = sorted(lst, key=lambda x: x[2])  
    return [x[:3] + ["third"] for x in sorted_lst]