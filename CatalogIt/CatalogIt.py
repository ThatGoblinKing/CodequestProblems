n_cases = int(input())
products = {}

def format(products, layerName = "None", layerNum = 0, currentLayers = ""):
    validKeys = []
    layerPrefix = "".join(["-" for i in range(layerNum)])
    for item in sorted(products[layerName]):
        if item in products.keys():
            validKeys.append(item)
            
    if len(validKeys) > 0:
        return "\n".join([format(products, key, layerNum + 1, f"{currentLayers}{layerPrefix}{key}\n") for key in validKeys])
    else:
        output = sorted([f"{layerPrefix}{item}" for item in products[layerName]])
        return currentLayers +"\n".join(output)

for _ in range(n_cases):
    line = input().rstrip()


    # change this line as needed:
    args = [val for val in line.split(",")]
    try:
        products[args[1]].append(args[0])
    except:
        products[args[1]] = [args[0]]
print(format(products))