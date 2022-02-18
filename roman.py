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
no = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
vals = {1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",
        400:"CD",500:"D",900:"CM",1000:"M"}


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

if __name__ == '__main__':
    print(convert(1000))
    print(convert(1904))
    print(convert(3999))
