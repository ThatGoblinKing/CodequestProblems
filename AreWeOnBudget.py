import math
import sys

def RoundHalfAway(num, decimalPoints):
    decimal = 10.0**(-decimalPoints) #makes a decimal you can use to multiply/divide (IE decimalPoints = 2, decimal = 0.01 )
    roundedNum = abs(int(num//decimal)) #puts digits you want to keep on the left side of the decimal (IE 1.394 = 139)
    finalDigit = roundedNum%10 #Gets the ones place
    if finalDigit >= 5:
        roundedNum += (10 - finalDigit) #rounds number up to nearest 10
    roundedNum *= decimal * (num/abs(num))#Multiplies Num back down to the right number of decimal points and makes it positive/negative
    return roundedNum

numberOfInputs = int(sys.stdin.readline().rstrip())
finalOutput = ""
for i in range(numberOfInputs):
    expenseCount = int(sys.stdin.readline().rstrip())
    budget = sys.stdin.readline().rstrip().split(" ")
    realExpenses = sys.stdin.readline().rstrip().split(" ")
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

