#https://lmcodequestacademy.com/problem/website-layout
#Estimated Time Spent: 56min
#Status: Incomplete
#Ideas to add to note document: GET NTH BIT FROM RIGHT BITWISE FUNCTION!!!

cases = int(input())
for _ in range(cases):
    elementsCount = int(input())
    elements = [0] * elementsCount
    maxPixels = 0
    for i in range(elementsCount):
        line = input()
        elements[i] = [int(val) for val in line.split()]
        maxPixels = max(maxPixels, sum(elements[i]))
    for i in range(len(elements)):
        binaryNumber = 0
        for j in range(elements[i][1]):
            binaryNumber = binaryNumber | (1 << (maxPixels - elements[i][0] - j - 1))
        elements[i] = binaryNumber
    finalState = False
    while not finalState:
        notOverlapping = True
        checkedNum = elements[0]
        copiedElements = elements[::]
        popElements = []
        for i in range(1, len(copiedElements)):
            if i == len(copiedElements) - 1:
                break
            for j in range(maxPixels):
                if (checkedNum >> maxPixels & 1 and copiedElements[i+1] >> maxPixels & 1):
                    notOverlapping = False
                    break
                else: 
                    pass
            if (notOverlapping):
                checkedNum += copiedElements[i+1]
                elements[0] = checkedNum
                popElements.append(i + 1)
        for value in sorted(popElements, reverse=True):
            elements.pop(value)
        if len(elements) == len(copiedElements):
            finalState = True
    for val in elements:
        print(f"{val:0{maxPixels}b}")