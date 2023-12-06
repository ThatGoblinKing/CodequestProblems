import math

def RoundHalfAway(num, decimalPoints):
    decimal = 10.0**(-decimalPoints)
    roundedNum = math.trunc(round(abs(num), decimalPoints + 1) / decimal) * decimal
    remainder = abs(num - math.trunc(num))
    if remainder >= decimal/10*5 and len(f"{remainder}") > decimalPoints + 1:
        roundedNum += decimal
    if roundedNum == -0.0 or num < 0:
        roundedNum *= -1
    return roundedNum

numberOfInputs = int(input())
finalOutput = ""
for i in range(numberOfInputs):
    expenseCount = int(input())
    budget = input().split(" ")
    realExpenses = input().split(" ")
    totalBudget = 0
    totalExpenses = 0
    costVariance = []
    for i in range(expenseCount):
        costVariance.append((float(budget[i]) - float(realExpenses[i])) * -1)
    average = 0
    for variance in costVariance:
        average += variance
    average = RoundHalfAway(average/expenseCount,2)
    if average == -0:
        average = 0
    finalOutput += f"{average:0.2f}\n"
print(finalOutput[:len(finalOutput)-1])

