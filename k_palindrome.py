from collections import defaultdict


def palindrone(s: str, k: int) -> int:
    """Can one create a palidrome by removing at most k chars"""
    d = defaultdict(int)

    for x in s:
        d[x] += 1

    odds = 0

    for v in d.values():
        if v % 2 == 1:
            odds += 1

    return odds - 1 - k <= 0


if __name__ == '__main__':
    # assert palindrone("abcdecba", 1)
    # assert palindrone("abcdeca", 2)
    assert not palindrone("acdcb", 1)
