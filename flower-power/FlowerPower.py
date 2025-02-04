#https://lmcodequestacademy.com/problem/flower-power
#Estimated Time Spent: 50min
#Status: Incorrect
#Ideas to add to note document: number system conversion function?
from contextlib import redirect_stdout
from functools import reduce
from io import StringIO

EXPECTED_OUTPUT = """\   \|/ \|/ \|/ \|/
 *   *- -*-  *   *-
    /|\ /|\      |\\
\|/ \|/ \|/
-*-  *   *
/|\\
\   \\
 *   *   *
"""

def getFirstRow(value : int) -> str:
    row = ""
    row += '\\' if value >= 1 else " "
    row += "|" if value >= 2 else " "
    row += "/" if value >= 3 else " "
    return row
def getMiddleRow(value : int) -> str:
    row = ""
    row += "-" if value >= 8 else " "
    row += "*"
    row += "-" if value >= 4 else " "
    return row
def getLastRow(value : int) -> str:
    row = ""
    row += "/" if value >= 7 else " "
    row += "|" if value >= 6 else " "
    row += '\\' if value >= 5 else " "
    return row

def makeBaseNine(n : int) -> str:
    digits = []
    while n:
        digits.append(int(n % 9))
        n //= 9
    return ''.join(reduce(lambda x,y: x + str(y), digits[::-1], ''))

def main():
    cases = int(input())
    for _ in range(cases):
        number = int(input())
        baseNineNum = makeBaseNine(number)
        currentRow = ""
        for digit in baseNineNum:
            currentRow += getFirstRow(int(digit)) + " "
        print(currentRow.rstrip())
        currentRow = ""
        for digit in baseNineNum:
            currentRow += getMiddleRow(int(digit)) + " "
        print(currentRow.rstrip())
        currentRow = ""
        for digit in baseNineNum:
            currentRow += getLastRow(int(digit)) + " "
        print(currentRow.rstrip())

f = StringIO()
with redirect_stdout(f):
    main()

finalOutput = f.getvalue()[:-1]

# print(len(finalOutput), len(EXPECTED_OUTPUT))

print(finalOutput)
# print(finalOutput == EXPECTED_OUTPUT)
# for i in range(len(finalOutput)):
#     if EXPECTED_OUTPUT[i] != finalOutput[i]:
#         print(f"\n\nPrinted: {ord(finalOutput[i])}\nExpected: {EXPECTED_OUTPUT[i]}")
#         break
#     else:
#         print(finalOutput[i], end="")
#
# print(f"\n\n\n\n\n{EXPECTED_OUTPUT}")
