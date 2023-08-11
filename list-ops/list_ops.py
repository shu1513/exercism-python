def append(list1, list2):
    list1.extend(list2)
    return list1


def concat(lists):
    finalls = []
    for each in lists:
        finalls = finalls + each
    return finalls


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return len(list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    import functools

    return functools.reduce(function, list, initial)


def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(item, initial)
    return initial


def reverse(list):
    list.reverse()
    return list
