def steps(number):
    # try
    if number <= 0 or not isinstance(
        number, int
    ):  # if number is smaller than 1 or not an integer raise value error
        raise ValueError("Only positive integers are allowed")
    sum = 0

    while number != 1:
        if number % 2 == 0:
            number = number / 2
            sum += 1
        else:
            number = number * 3 + 1
            sum += 1
    return sum


print(steps(31))
