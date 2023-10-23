A = 0
D = 2
F = 3
G = 4
V = 5
X = 6
table = [[], [], [], [], [], []]
transposeTable = []
testCases = int(input())
for i in range(testCases):
    for i in range(6):
        table[i] = [*input()]
    keyword = input()
    alphabeticKeyword = ''.join(sorted(keyword))
    encryptedMessage = input()
    transposeTable = [[], [], [], [], [], []]
    for i in range(len(encryptedMessage)):
        print(i, encryptedMessage[i])
        if i%6 == 0:
            columnNumber = 
        elif i%6 == 1:
        elif i%6 == 2:
        elif i%6 == 3:
        elif i%6 == 4:
        else:
            columnNumber = 
        transposeTable[columnNumber].append(encryptedMessage[i])

    print(transposeTable)