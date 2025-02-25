#https://lmcodequestacademy.com/problem/dollar-bill-poker

# START TIME: 8:52
# INTERRUPTION START: 8:55
# INTERRUPT END: 9:03
# INTERRUPTION START 9:08
# INTERRUPTION END: 9:22
# END 9:46
# DNF. EDGE CASE ERROR

from enum import Enum
from typing import List
from contextlib import redirect_stdout
from io import StringIO


class Hands(int, Enum):
    FIVE_KIND = 1
    FOUR_KIND = 2
    FULL_HOUSE = 3
    STRAIGHT = 4
    THREE_KIND = 5
    TWO_PAIR = 6
    PAIR = 7
    HIGH = 8

def two_pair(digits: List[int]) -> bool:
    pairs: int = 0
    for digit in digits:
        if (digit == 2):
            pairs += 1
    return pairs >= 2

def straight(digits: List[int]) -> bool:
    longest_sequence = 0
    temp_sequence = 0
    for digit in digits:
        if digit != 0:
            temp_sequence += 1
        else:
            temp_sequence = 0
        if temp_sequence > longest_sequence:
            longest_sequence = temp_sequence
    return longest_sequence >= 5

def get_highest(digits: List[int]):
    if 5 in digits:
        return "FIVE OF A KIND"
    elif 4 in digits:
        return "FOUR OF A KIND"
    elif 3 in digits and 2 in digits:
        return "FULL HOUSE"
    elif straight(digits):
        return "STRAIGHT"
    elif 3 in digits:
        return "THREE OF A KIND"
    elif two_pair(digits):
        return "TWO PAIR"
    elif 2 in digits:
        return "PAIR"
    else:
        for i in range(8, 0, -1):
            if digits[i] > 0:
                return str(i + 1)

EXPECTED_OUTPUT = """14912276 = TWO PAIR
99027737 = FULL HOUSE
39217860 = 9
59977643 = STRAIGHT
58276501 = PAIR
77437751 = FOUR OF A KIND
03999299 = FIVE OF A KIND
12145671 = THREE OF A KIND
12340076 = 7
98764115 = STRAIGHT
11223344 = TWO PAIR"""

f = StringIO()
with redirect_stdout(f):
    cases = int(input())
    for _ in range(cases):
        line = input().strip()
        digits_repeating = [0] * 10
        for character in line:
            digits_repeating[int(character)] += 1
        digits_repeating = digits_repeating[1:]
        print(digits_repeating)
        pattern = get_highest(digits_repeating)
        print(f"{line} = {pattern}")
s = f.getvalue()
print(s.strip())