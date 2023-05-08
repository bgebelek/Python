#Practice Python - Exercise 5 - List Overlap


def common_list(list1, list2):
        return list(set([x for x in list1 if x in list2]))


print(common_list([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
