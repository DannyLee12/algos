"""
An encoded string (s) is given, the task is to decode it.
The pattern in which the strings are encoded is as follows.

<count>[sub_str] ==> The substring 'sub_str'
                      appears count times.

Examples:

Input : str[] = "1[b]"
Output : b

Input : str[] = "2[ab]"
Output : abab

Input : str[] = "2[a2[b]]"
Output : abbabb

Input : str[] = "3[b2[ca]]"
Output : bcacabcacabcaca

"""


def extract(s: str, text: str="") -> str:
    """Extract a repeated substring recursively"""
    def extract_one(s):
        text = ""
        for i, x in enumerate(s):
            if x.isalpha():
                text += x
            if x.isnumeric():
                multiplier = x
                i += 1
                while s[i].isnumeric():
                    multiplier += s[i]
                    i += 1
                break

        return text + int(multiplier) * s[s.index("[") + 1: s.index("]")]

    while "[" in s:
        for i, x in enumerate(s):
            if x == "[":
                open = i
            elif x == "]":
                s = s[:open - 1] + extract_one(s[open-1:i+1]) + s[i+1:]
                break

        extract(s)

    return s


if __name__ == '__main__':
    assert extract("3[b2[ca]]") == "bcacabcacabcaca"