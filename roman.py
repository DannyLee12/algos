"""
Given a number, find its corresponding Roman numeral.
Examples:

Input : 9
Output : IX

Input : 40
Output : XL

Input :  1904
Output : MCMIV

Idea here is to recursively split the number from largest to smallest until
it's 0 and then return the string
"""
from random import randint


no = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
vals = {1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",
        400:"CD",500:"D",900:"CM",1000:"M"}
new_vals = dict([(value, key) for key, value in vals.items()])


def convert(input: int, roman: str=None) -> str:
    """Convert an integer to Roman Numerals"""
    roman = roman or ""
    if not input:
        return roman

    for x in no:
        if input in vals:
            roman += vals[input]
            remainder = 0
            break
        if x < input:
            count = input // x
            remainder = input % x
            roman += count * vals[x]
            break

    return convert(remainder, roman)


def convert_back(roman: str) -> int:
    """Convert from roman numerals to decimal"""

    # Two options - two digits (i.e) IV CM etc etc. Or one digit
    # Therefore, always check the order of the numbers.
    value = 0
    i = 0
    while i < len(roman):
        if roman[i: i +2] in new_vals:
            value += new_vals[roman[i:i + 2]]
            i += 2
        else:
            value += new_vals[roman[i]]
            i += 1

    return int(value)


if __name__ == '__main__':
    print(convert(1000))
    print(convert(1904))
    print(convert(3999))

    print(convert_back("MCMIV"))

    for _ in range(50):
        val = randint(1, 3999)
        assert val == convert_back(convert(val))
