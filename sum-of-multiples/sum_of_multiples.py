def sum_of_multiples(limit, multiples):
    nset = set()
    for each in multiples:
        if each <= 0:
            continue
        else:
            i = 1
            while each * i < limit:
                nset.add(each * i)
                i += 1
    return sum(nset)
