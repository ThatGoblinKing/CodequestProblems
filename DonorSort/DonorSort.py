testCases = int(input())
finalOutput = ""


for i in range(testCases):
    lastYear = []
    bothYears = []
    thisYear = []
    lastDonors = input().split(",")
    currentDonors = input().split(",")
    for donor in lastDonors:
        if donor not in currentDonors:
            lastYear.append(donor)
        else:
            bothYears.append(donor)
    for donor in currentDonors:
        if donor not in lastDonors:
            thisYear.append(donor)
    finalOutput += f"{','.join(sorted(lastYear))}\n{','.join(sorted(bothYears))}\n{','.join(sorted(thisYear))}\n"
print(finalOutput.strip())