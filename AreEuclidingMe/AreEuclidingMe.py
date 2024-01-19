numberOfInputs = int(input())
numbers = []
for i in range(numberOfInputs):
    numbers.append(input().split(","))
for pair in numbers:
    pair[0] = int(pair[0])
    pair[1] = int(pair[1])
    difference = None
    
    while difference != 0:
        if pair[0] > pair[1]:
            difference = pair[0] - pair[1]
            print(f"{pair[0]}-{pair[1]}={difference}")
            pair[0] = difference
        else:
            difference = pair[1] - pair[0]
            print(f"{pair[1]}-{pair[0]}={difference}")
            pair[1] = difference
    if pair[0] == 1 or pair[1] == 1:
        print("COPRIME")
    else:
        print("NOT COPRIME")