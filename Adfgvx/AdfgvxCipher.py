A = 0
D = 1
F = 2
G = 3
V = 4
X = 5
table = [[], [], [], [], [], []]
testCases = int(input())
finalOutput = ""
for i in range(testCases):
    for i in range(6):
        table[i] = [*input()]
    keyword = input()
    alphabeticKeyword = ''.join(sorted(keyword))
    encryptedMessage = input()
    keywordLen = len(keyword)
    rowCount = int(len(encryptedMessage) / keywordLen)
    transposeTable = []
    alphabeticalTransposeTable = []
    for i in range(keywordLen):
        transposeTable.append([])
        alphabeticalTransposeTable.append([])
    cypheredLetters = ''
    hangingChars = ''
    for i in range(len(encryptedMessage)):
        columnNumber = i%keywordLen
        if i < (keywordLen * rowCount):
            transposeTable[columnNumber].append(encryptedMessage[i])
        else:
            hangingChars += encryptedMessage[i]

    charColumns = ''.join(sorted(keyword[0:len(hangingChars)]))

    for i in range(len(hangingChars)):
        transposeTable[alphabeticKeyword.find(charColumns[i])].append(hangingChars[i])
    for i in  range(keywordLen):
        alphabeticalTransposeTable[keyword.find(alphabeticKeyword[i])] = transposeTable[i]
    addedChars = 0
    for i in range(rowCount + 1):
        for j in range(len(transposeTable)):
            try:
                cypheredLetters += alphabeticalTransposeTable[j][i]
                if (addedChars + 1)%2 == 0 and cypheredLetters[-1] is not None:
                 cypheredLetters+= "_"
                addedChars += 1
            except:
                pass
    letterPairs = cypheredLetters.split('_')

    decyphered = ""
    for pair in letterPairs:
        if len(pair) == 2:
            if pair[0] == 'A':
                x = A
            elif pair[0] == 'D':
                x = D
            elif pair[0] == 'F':
                x = F
            elif pair[0] == 'G':
                x = G
            elif pair[0] == 'V':
                x = V
            else:
                x = X

            if pair[1] == 'A':
                y = A
            elif pair[1] == 'D':
                y = D
            elif pair[1] == 'F':
                y = F
            elif pair[1] == 'G':
                y = G
            elif pair[1] == 'V':
                y = V
            else:
                y = X
            finalOutput += table[x][y]
    finalOutput += "\n"
finalOutput = finalOutput[:(len(finalOutput) - 1)]
print(finalOutput)