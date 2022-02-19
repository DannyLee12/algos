"""Given an integer array and a positive integer k, count all distinct pairs
with differences equal to k. """


def count_distinct(l: list, k: int) -> set:
    """Return the unique ways to make k from two values in l"""
    # O(N^2)
    vals = set()
    for i, x in enumerate(l):
        for j, y in enumerate(l):
            if i == j:
                continue
            if abs(x - y) == k:
                vals.add(tuple(sorted([x, y])))

    return vals


def count_distinct_faster(l: list, k: int) -> set:
    """Use a better approach"""
    vals = set()
    l = set(l)  # O(N)
    for x in l:  # O(N)
        if x - k in l:  # O(1)
            vals.add(tuple(sorted([x, x - k])))

    return vals


def count_distinct_sorted(l: list, k: int) -> set:
    """Try sorting to get another answer"""
    l.sort()  # N log N
    vals = []
    for i, x in enumerate(l[:-1]):  # N
        counter = 1 + i

        while l[counter] - x <= k:
            if l[counter] - x == k:
                vals.append(sorted([x, l[counter]]))
                break
            counter += 1
            if counter > len(l) - 1:
                break

    return vals




if __name__ == '__main__':
    print(count_distinct([1, 5, 3, 4, 2], 3))
    print(count_distinct([8, 12, 16, 4, 0, 20], 4))

    print(count_distinct_faster([1, 5, 3, 4, 2], 3))
    print(count_distinct_faster([8, 12, 16, 4, 0, 20], 4))

    print(count_distinct_sorted([1, 5, 3, 4, 2], 3))
    print(count_distinct_sorted([8, 12, 16, 4, 0, 20], 4))