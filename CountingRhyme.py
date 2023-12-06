def checkSafety(skips, landsOn, startsOn, groupSize):
    if (startsOn + landsOn + skips) % groupSize == 0:
        return False
    elif skips == 4:
        return True
    else:
        return checkSafety(skips + 1, landsOn + 1 % groupSize, startsOn + 1 % groupSize + 1, groupSize)
numberOfInputs = int(input())
wordCounts = []
groupCounts = []
for i in range(numberOfInputs):
    splitString = input().split(" ")
    groupCounts.append(int(splitString[0]))
    wordCounts.append(int(splitString[1]))
for i in range(len(groupCounts)):
    landingOn = (wordCounts[i] / groupCounts[i]) + wordCounts[i] % groupCounts[i]
    for i in range(groupCounts[i]):
        if checkSafety(0, landingOn, i, groupCounts[i]) == True:
            safeStarter = i
            break
        else:
            safeStarter = -1
    print(safeStarter)

