
EXPECTED_OUTPUT = """153/2 50 153/2
199/2 199/2
50 75 95 95 95"""

testCases = int(input())

finalOutput = ""
for case in range(testCases):
    line = input().rstrip()
    totalFuel, tankCount = (int(val) for val in line.split(" "))
    fullTank = [False for i in range(tankCount)]
    line = input().rstrip()
    tankSizes = [int(val) for val in line.split(" ")]
    
    for i in range(len(tankSizes)):
        if totalFuel/tankCount > tankSizes[i]:
            totalFuel -= tankSizes[i]
            tankCount -= 1
            fullTank[i] = True
            
    for i in range(len(tankSizes)):
        if fullTank[i] == True:
            finalOutput += f"{tankSizes[i]} "
        else:
            commonFactors = [i for i in range(1, tankCount+1) if (tankCount/i % 1) == 0 and (totalFuel/i % 1) == 0]
            greatestCommonDenominator = sorted(commonFactors)[-1]
            if totalFuel/tankCount%1 == 0:
                finalOutput += f"{int(totalFuel/tankCount)} "
            else:
                finalOutput += f"{int(totalFuel/greatestCommonDenominator)}/{int(tankCount/greatestCommonDenominator)} "
    finalOutput = finalOutput.rstrip() + "\n"
print(finalOutput.strip())