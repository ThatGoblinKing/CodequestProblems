numberOfInputs = int(input())
lines = ["","","","","","","","","",""]

for i in range(numberOfInputs):
    generations = int(input())
    for j in range(10):
        lines[j] = input()
    for j in range(generations):
        