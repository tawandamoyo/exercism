def square(number):
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    total = 0
    for number in range(64):
        total = total + (2 ** number)
    return total
