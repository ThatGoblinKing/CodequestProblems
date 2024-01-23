testCases = int(input())
finalOutput = ""

for case in range(testCases):
    line = input().rstrip()
    
    arraySize = [int(val) for val in line.split(" ")]
    wrongArray = [["" for j in range(arraySize[1])] for i in range(arraySize[0])]
    correctArray = [["" for j in range(arraySize[0])] for i in range(arraySize[1])]
    
    for i in range(arraySize[0]):
        line = input().rstrip()
        wrongArray[i] = line.split(',')
        
    for x in range(arraySize[0]):
        for y in range(len(wrongArray[x])):
            correctArray[y][x] = wrongArray[x][y]
    for row in correctArray:
        finalOutput += ','.join(row) + "\n"
print(finalOutput.strip())