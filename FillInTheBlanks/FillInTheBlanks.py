def replaceBracket(line, currentOutput=""):
    
    if "[" and "]" not in line:
        # return everything that comes before it, the current line, and a new line to seperate it
        return currentOutput + line + "\n"
    else:
        firstBracket = line.index('[')
        secondBracket = line.index(']') + 1

        value = data[line[firstBracket + 1:secondBracket - 1]]

        return replaceBracket(line[secondBracket:], currentOutput + line[:firstBracket] + value)


finalOutput = ""

n_cases = int(input())

for _ in range(n_cases):

    line = input().rstrip()

    dataLength, letterLength = [int(val) for val in line.split(" ")]

    data = {}
    for i in range(dataLength):
        name, value = input().rstrip().split(": ")
        data[name] = value

    letter = [input() for i in range(letterLength)]

    for line in letter:
        finalOutput += replaceBracket(line)
else:
    print(finalOutput.rstrip())
