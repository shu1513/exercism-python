def label(colors):
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
    number = 0
    first_number = colorlist.index(colors[0]) * 10 + colorlist.index(colors[1])
    zero_number = 10 ** colorlist.index(colors[2])
    final_number = first_number * zero_number
    if final_number < 1000:
        return str(final_number) + " ohms"
    elif 1000 < final_number < 1000000:
        return str(final_number // 1000) + " kiloohms"
    elif 1000000000 < final_number < 1000000000:
        return str(final_number // 1000000) + " megaohms"
    else:
        return str(final_number // 1000000000) + " gigaohms"
