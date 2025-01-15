#https://lmcodequestacademy.com/problem/highlight-of-my-day
import re

# correctOutput = """(255,128,230) (77,77,77) (102,102,255) (230,26,255) (102,51,51) (153,230,26)
# (128,255,128) (128,128,0) (128,128,0) (128,128,0) (128,128,0) (179,230,179)
# (255,77,102) (128,128,0) (115,103,128) (179,90,64) (128,128,0) (0,26,102)
# (77,102,179) (128,128,0) (115,154,26) (128,128,0) (128,128,0) (230,26,204)
# (102,230,179) (128,128,0) (128,128,0) (128,128,0) (153,153,179) (230,102,153)
# (230,128,128) (153,102,179) (77,102,179) (230,153,77) (26,153,204) (153,153,179)
# (26,153,153) (51,51,255) (51,51,255) (51,51,255) (77,26,128)
# (51,51,255) (51,51,255) (77,128,243) (51,51,255) (51,51,255)
# (51,51,255) (51,26,166) (77,115,192) (115,128,243) (51,51,255)
# (51,51,255) (51,51,255) (64,90,243) (51,51,255) (51,51,255)
# (153,51,230) (51,51,255) (51,51,255) (51,51,255) (26,128,179)"""


from RoundingFunction import round_half_away

def checkSurroundPixels(mask, x, y)-> bool:
    for i in range(9):
        try:
            if mask[x + i%3 - 1][y + i//3 - 1]:
                return True
        except(IndexError):
            pass
    else:
        return False


finalString = ""

cases = int(input())
for _ in range(cases):
    line = [int(re.sub(r"[()]", "", value)) for value in input().strip().split(',')]
    highlightColor = line
    line = input()
    width, height = [int(val) for val in line.split()]
    mask = []
    img = []
    for i in range(height):
        mask.append([bool(int(val)) for val in input().strip().split()])
    for i in range(height):
        img.append([[int(re.sub(r"[()]", "", subval)) for subval in val.split(',')] for val in input().strip().split()])
    outlineIndices = []
    maskIndices = []
    for i in range(height):
        for j in range(width):
            if mask[i][j]:
                maskIndices.append([i, j])
            elif checkSurroundPixels(mask, i, j):
                outlineIndices.append([i, j])
    for index in maskIndices:
        for i in range(3):
            img[index[0]][index[1]][i] = int(round_half_away((img[index[0]][index[1]][i] * .5) + (.5 * highlightColor[i]), 0))
    for index in outlineIndices:
        try:
            img[index[0]][index[1]] = highlightColor[:]
        except:
            print(index)
            print(img[index[0]])
            print(" ".join(str(img)))
    formattedList = []
    for i in range(height):
        for j in range(width):
         formattedList.append(f'({",".join([str(val) for val in img[i][j]])})')
    for i in range(1, height + 1):
        finalString += " ".join(formattedList[width * (i-1):width * i]) + "\n"
# print(finalString.strip() == correctOutput)
# for i in range(len(finalString.strip())):
#     if not finalString[i] == correctOutput[i]:
#         # print(finalString[0:i+1])
#         # print(correctOutput[0:i+1])
#         break

print(finalString.strip())