def union_multiple_sets(*sets):
    # sets = {1, 2}, {3, 4}, {5, 6}
    set3 = set() # set3 = {}
    for i in sets:
        set3 = set3.union(i) # i = 0 {1,2}
                            #  i = 1 {1,2} | {3,4}
    return set3
result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}