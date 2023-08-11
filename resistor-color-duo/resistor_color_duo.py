def value(colors):
    colorlist = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    numberlist = []
    for color in colors[:2]:
        numberlist.append(colorlist.index(color))
    return numberlist[0] * 10 + numberlist[1]
