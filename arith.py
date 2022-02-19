"""Given a string of numbers, the task is to find the maximum value from the
string, you can add a ‘+’ or ‘*’ sign between any two numbers."""


def arith(number: str) -> int:
    """Return the max value by adding + or *"""
    # Always add a *, unless it's 0 or 1
    total = int(number[0])

    for x in list(map(int, number[1:])):
        if total == 0 or total == 1:
            total += x
        elif x == 0 or x == 1:
            total += x
        else:
            total *= x

    return total


if __name__ == '__main__':
    print(arith("01231"))
    print(arith("891"))
