def checkSurroundings(startingLine: int, startingIndex: int, map: list[str]):

    surroundings = 0
    line = startingLine
    index = startingIndex

    for i in range(9): #We're checking a 3 by 3 area, 3 x 3 = 9
        try:
            line = startingLine + (i//3 - 1)
            #switches between -1, 0, and 1 each time i goes up 3
            index = startingIndex + (i%3 - 1)
            #switches between -1, 0, and 1 when i goes up by one, resets every time i goes up 3

            if map[line][index] == "1": #Check if alive
                if line == startingLine and index == startingIndex: #Is this the cell we're checking?
                    surroundings += 10 #This is an easily reversable number to check whether or not the original cell is alive without using a seperate variable
                else:
                    surroundings += 1 #increases count of how many alive cells surround this one
        except IndexError: #If we're checking a cell on the edges we can get an out of bounds exception
            continue

    return surroundings

#Checking how many test cases we're doing
testCases = int(input().rstrip())

#Setting variables

for i in range(testCases):
    generations = int(input().rstrip())
    #finalOutput += f"{testCases}\n{generations}\n"  #you'll have to get rid of this when submitting.
    lines = [input().rstrip() for j in range(10)]
    for j in range(generations):
        currentGen = lines[:]
        for k in range(100): #We're checking 10 lines of 10 characters each, therefore we're checking 100 characters
            currentLine = k//10 #divide by ten, drop the remainder, get the line number
            currentIndex = k%10 #How much between current number and next 10? gets the current index
            alive = False
            surrounds = checkSurroundings(currentLine, currentIndex, currentGen)
            if surrounds >= 10: #The highest surrounds can be without being alive is 8 so this won't ever give a false positive
                alive = True
                surrounds -= 10
            if alive and surrounds == 2 or surrounds == 3:
                pass
            elif surrounds == 3:
                lines[currentLine] = lines[currentLine][:currentIndex] + "1" + lines[currentLine][currentIndex + 1:] #Replaces the current character with a 1
            else: #If it has less than 2 live neighbors, or more than 3 live neighbors it dies. If it is dead, it'll stay dead since it does not have exactly 3 living neighbors
                lines[currentLine] = lines[currentLine][:currentIndex] + "0" + lines[currentLine][currentIndex + 1:] #Replaces the current character with a 0
    print("\n".join(lines).strip()) #Add the final generation to a string) += "\n".join(lines) + "\n" #Add the final generation to a string
 #print output, remove excess whitespace