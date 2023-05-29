#!/usr/bin/python3

def safe_print_list(list, x):
    count = 0
    res = []
    for i in list[ : x]:
        try:
            res.append(i)
        except TypeError:
            print('Cannot perform operation on different types', arg)
        else:
            count+=1
    

    print(*res, sep = "")
    return count
