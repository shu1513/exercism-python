def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        grains_on_square = 2 ** (number - 1)
        return grains_on_square


def total():
    sum = 0
    for i in range(64):
        sum = sum + 2 ** (i)
    return sum
