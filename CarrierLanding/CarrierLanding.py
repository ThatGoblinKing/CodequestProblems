testCases = int(input())
finalOutput = ""
CLEAR = "{}, Clear To Land!"
ABORT = "{}, Abort Landing!"
X = 0
Y = 1

for case in range(testCases):
    aircraftSections = int(input().rstrip())
    for section in range(aircraftSections):
        planeName = input().rstrip()

        lines = [input().rstrip() for i in range(3)]
        
        currentOutput = ""
            
        # change this line as needed:
        aircraftCoords, startCoords, endCoords = [val for val in [line.split() for line in lines]]

        aircraftCoords, startCoords, endCoords = [int(val) for val in aircraftCoords[0].split(',')], [int(val) for val in startCoords[0].split(',')], [int(val) for val in endCoords[0].split(',')]

        startSlope, endSlope = (startCoords[Y] - aircraftCoords[Y])/(startCoords[X] - aircraftCoords[X]), (endCoords[Y] - aircraftCoords[Y])/(endCoords[X] - aircraftCoords[X])

        currentOutput = CLEAR if -1.6 <= startSlope <= -0.8 and -1.6 <= endSlope <= -0.8 else ABORT

        finalOutput += currentOutput.format(planeName) + "\n"
print(finalOutput.rstrip())