def color_code(color):
    global code
    code = list(
        (
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
        )
    )

    return code.index(color)  # a


def colors():
    return code
