#https://lmcodequestacademy.com/problem/halves-and-doubles
from typing import Union
from contextlib import redirect_stdout
import io

OUTPUT = """10 20 ***
5 40
2* 80 ***
1 160
200
11 6
5* 12
2* 24 ***
1 48
66
60 200 ***
30 400 ***
15 800
7* 1600
3* 3200
1* 6400
12000"""

def halfAndDoubleMult(num1: Union[float, int], num2: int) -> int:
    firstOutputHalf = f"{int(num1)}* " if int(num1) != num1 else f"{int(num1)} "
    num1 = int(num1)
    if num1 == 1:
        multOutput = firstOutputHalf + f"{num2}"
        print(multOutput)
        return int(num2)
    elif num1 % 2 == 0:
        multOutput = firstOutputHalf + f"{num2} ***"
        print(multOutput)
        return 0 + halfAndDoubleMult(num1 / 2, num2 * 2)
    else:
        multOutput = firstOutputHalf + f"{num2}"
        print(multOutput)
        return int(num2) + halfAndDoubleMult(num1/2, num2*2)


f = io.StringIO()
with redirect_stdout(f):
    cases = int(input())
    for _ in range(cases):
        line = input()
        val1, val2 = (int(val) for val in line.split(" "))
        print(halfAndDoubleMult(val1, val2))
s = f.getvalue().strip()
print(s)