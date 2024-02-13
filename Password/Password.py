n_cases = int(input())
finalOutput = ""
upper = 0
lower = 1
number = 2
special = 3


for _ in range(n_cases):
    repeating = False
    requirements = [False for i in range(4)]
    line = input().rstrip()

    if len(line) < 8:
        finalOutput += "INVALID\n"
        continue

    for i in range(len(line)):
        character = line[i]
        if character.isupper():
            requirements[upper] = True
        elif character.islower():
            requirements[lower] = True
        elif character.isnumeric():
            requirements[number] = True
        elif not character.isalnum():
            requirements[special] = True

        if line[i-2:i + 1] == character * 3:
            requirements = [False for i in range(4)]
            break

        requirementsMet = 0

    for value in requirements:
        if value:
            requirementsMet += 1

    finalOutput += "VALID\n" if requirementsMet >= 3 else "INVALID\n"
print(finalOutput.rstrip())
