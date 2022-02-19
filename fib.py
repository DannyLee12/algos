"""Given an array with positive number the task is that we find largest subset
from array that contain elements which are Fibonacci numbers."""
from functools import lru_cache


@lru_cache()
def fibonacci(n: int):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n - 2)


if __name__ == '__main__':
    input = [1, 4, 3, 9, 10, 13, 7]
    input = [0, 2, 8, 5, 2, 1, 4,
             13, 23]

    fibs = {fibonacci(i) for i in range(100)}
    max_val = fibonacci(99)

    subset = []
    counter = 100
    for x in input:
        while x > max_val:
            max_val = fibonacci(counter)
            fibs.add(max_val)
            counter += 1
        if x in fibs:
            subset.append(x)

    print(subset)



