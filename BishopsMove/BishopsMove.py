#https://lmcodequestacademy.com/api/static/problems/bishops-move

testCases = int(input())
finalOutput = ""
EXPECTED_OUTPUT = "Yes\nYes\nNo"

for case in range(testCases):
    line = input().rstrip()
    line2 = input().rstrip()
    line3 = input().rstrip()

    # change this line as needed:
    mapSize = [int(val) for val in line.split(",")]
    startingPos = [int(val) for val in line2.split(",")]
    endPos = [int(val) for val in line3.split(",")]

    inBounds = 0 < endPos[0] <= mapSize[0] and 0 < startingPos[0] <= mapSize[0] and 0 < endPos[1] <= mapSize[1] and 0 < startingPos[1] <= mapSize[1]
    finalOutput += "Yes\n" if abs(endPos[0] - startingPos[0]) == abs(endPos[1] - startingPos[1]) and inBounds else "No\n"
print(finalOutput.rstrip())