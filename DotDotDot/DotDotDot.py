testCases = int(input())
finalOutput = ""

for case in range(testCases):
    line = input().rstrip().lower()
    unusedAsciiCharacters = ord("a") - 1
    clicks = 0
    for character in line:
        clicks += ord(character) - unusedAsciiCharacters
    finalOutput += f"{clicks}\n"
print(finalOutput.rstrip())