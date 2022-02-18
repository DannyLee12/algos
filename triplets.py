"""Given an array of distinct elements. The task is to find triplets in the
array whose sum is zero."""


def triplets(l: list) -> list:
    """Return triplets that add up to 0"""
    # Since for three values to add up to 0
    # x, y & z exist such that
    # x = - (y+z)
    triples = set()
    n = len(l)
    l.sort()
    for x in l:
        if x > 0:
            break
        # start at the smallest and biggest number
        i = - 1
        j = - 2
        while l[i] + l[j] >= - x:
            if l[i] + l[j] == - x:
                triples.add(",".join(list(map(str, sorted([x, l[i], l[j]])))))
            i -= 1
            if i == x:
                j -= 1

    return triples

if __name__ == '__main__':
    print(triplets([0, -1, 2, -3, 1]))
    print(triplets([1, -2, 1, 0, 5]))