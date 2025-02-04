numberOfWords = int(input())
start = ""
for i in range(numberOfWords):
    tested = input()
    groupSize, wordCount = tested.split(" ")
    wordCount = int(wordCount) - 1
    groupSize = int(groupSize)

    group = []
    for i in range(groupSize):
        group.append(i)
    groupTemplate = group
    safe = False
    startingNumber = 0
    currentMember = 0
    while not safe:
        print(startingNumber)
        group = groupTemplate
        if startingNumber > groupSize - 1:
            print("Something BAD happened :(")
            safe = True
            continue
        currentMember = 0 + startingNumber
        while len(group) > 1:
            #if 0 not in group:
            #   break
            group.pop((currentMember+wordCount)%len(group))
            currentMember = (currentMember+wordCount)
        if group[0] == 0:
            safe = True
        else:
            startingNumber += 1
    start += str(startingNumber) + "\n"

print(start)