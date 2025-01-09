#https://lmcodequestacademy.com/problem/flower-power
#Estimated Time Spent: 50min
#Status: Incorrect
#Ideas to add to note document: number system conversion function?

from functools import reduce

EXPECTED_OUTPUT = "\\   \\|/ \\|/ \\|/ \\|/\n *   *- -*-  *   *-\n    /|\\ /|\\      |\\\n\\|/ \\|/ \\|/\n-*-  *   *\n/|\\\n\\   \\\n *   *   *\n\n"

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
finalOutput = ""
cases = int(input())
for _ in range(cases):
    number = int(input())
    baseNineNum = makeBaseNine(number)
    flower = ""
    currentRow = ""
    for digit in baseNineNum:
        currentRow += getFirstRow(int(digit)) + " "
    flower += currentRow.rstrip() + "\n"
    currentRow = ""
    for digit in baseNineNum:
        currentRow += getMiddleRow(int(digit)) + " "
    flower += currentRow.rstrip() + "\n"
    currentRow = ""
    for digit in baseNineNum:
        currentRow += getLastRow(int(digit)) + " "
    finalOutput += flower + currentRow.rstrip() + "\n"

print(finalOutput)