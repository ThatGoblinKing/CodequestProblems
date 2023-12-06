#https://lmcodequestacademy.com/api/static/problems/ascii-squares

def isSquare(lines, currentIndex):
    currentLine = lines[currentIndex]
    for i in range (currentLine):
        
        
        pass
    '''currentLine = lines[currentIndex].replace("|", " ")
    if currentLine[0] == " ":
        currentLine = currentLine[1:len(lines[currentIndex]) - 1]
    try:
        testedRow = lines[currentIndex + 1][:len(currentLine) * 2 + 1] #sets Tested row to the next line, but only up until the length of currentLine.
    except:
        return 0
    walllessRow = testedRow.replace("|", " ")[1:len(testedRow) - 1]
    if walllessRow == currentLine and testedRow.count("|") == len(currentLine) - 2:
        return (testedRow.count("|") - 1)
    else:
        return 0'''

numberOfInputs = int(input())
for i in range(numberOfInputs):
    numberOfLines = int(input())
    lines = []
    previousLine = ""
    for i in range(numberOfLines):
        lines.append(input())
        width = 0
    squares = 0
    for i in range(len(lines)):
         squares += isSquare(lines, i)
print(squares)