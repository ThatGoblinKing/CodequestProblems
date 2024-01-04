numberOfWords = int(input())
start = ""
for i in range(numberOfWords):
    tested = input()
    groupSize, wordCount = tested.split(" ")
    wordCount = int(wordCount)
    groupSize = int(groupSize)

    out = []
    for i in range(groupSize):
        out.append(False)
    safe = False
    startingNumber = 0
    while not safe:
        for i in range(groupSize):
            out[i] = False
        currentWord = 0
        skips = 0
        while skips < groupSize:
            while currentWord < wordCount:
                if out[0] == True:
                    break
                if not out[(currentWord+startingNumber+skips)%groupSize] == True:
                    out[(currentWord+startingNumber+skips)%groupSize] = True
                    currentWord += 1
                else: 
                    skips += 1
        safe = not out[0]
        startingNumber += 1
    start += str(startingNumber) + "\n"

print(start)