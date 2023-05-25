def transform(legacy_data):
    finaldict = {}
    result = {}
    for number, letterlist in legacy_data.items():
        # this gives me each individual key:value pairs
        # such as (1,[a,b,c])
        for letter in letterlist:
            finaldict[letter.lower()] = number
    temp = sorted(finaldict.keys())
    for i in temp:
        result[i] = finaldict[i]
    return result
