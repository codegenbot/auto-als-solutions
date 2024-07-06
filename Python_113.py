def odd_count(lst):
    return [
        "the number of odd elements {}n the str{}ng {} of the {}nput.".format(
            len([i for i in s if int(i) % 2]), s.index(str(i)), s, lst.index(s)
        )
        for s in lst
    ]