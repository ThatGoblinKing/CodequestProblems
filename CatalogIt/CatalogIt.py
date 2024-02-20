n_cases = int(input())
products = {}
finalOutput = ""
EXPECTED_OUTPUT = "All Products\n-Aeronautic Products\n--Fighter Planes\n---F-22 Raptor\n---F-35 Lightning 2\n-Space Products\n--Manned Spacecraft\n---Orion\n--Satellites\n---A2100\n---GPS"



def format(products, layerName="None", layerNum=0, currentLayers=""):
    validKeys = []
    layerPrefix = "".join(["-" for i in range(layerNum)])
    for item in sorted(products[layerName]):
        if item in products.keys():
            validKeys.append(item)
    if len(validKeys) > 0:

        return "\n".join([format(products, key, layerNum + 1, f"{currentLayers}{layerPrefix}{key}\n") for key in validKeys])
    else:
        output = sorted(
            [f"{layerPrefix}{item}" for item in products[layerName]])
        products[args[1]] = [args[0]]
        return currentLayers + "\n".join(output)


for _ in range(n_cases):

    line = input().rstrip()
    # change this line as needed:
    args = [val for val in line.split(",")  ]
    try:
        products[args[1]].append(args[0])
    except:
        lines = format(products).strip().split("\n")

repeatLines = []
for i in range(len(lines)):
    if lines[i] in lines[:i]:
        repeatLines.append(i)
deletedItems = 0
for index in repeatLines:
    lines.pop(index - deletedItems)
    deletedItems += 1

finalOutput = "\n".join(lines)
print(finalOutput.strip())
