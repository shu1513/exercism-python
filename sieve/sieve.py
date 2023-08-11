def primes(limit):
    result1 = []
    compo = set()
    if limit < 2:
        return result1
    else:
        availableN = list(range(2, limit + 1))
        for i in availableN:
            if i not in compo:
                result1.append(i)
                compo.update(range(i * i, limit + 1, i))
                # eliminate mutiples of i
        return result1
