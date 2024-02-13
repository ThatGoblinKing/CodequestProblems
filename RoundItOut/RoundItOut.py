def getResult(result, n_digits):
    result /= 10**n_digits
    if int(result) == result:
        result = int(result)
        n_digits = 0
        return f"{result:.{n_digits}f}\n"
    else:
        return f"{result}\n"

def halfUp(val: float, n_digits: int = 0):
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return getResult(result, n_digits)

def halfDown(val: float, n_digits: int = 0):
    val *= 10**n_digits
    result = int(val + (0.5 if val > 0 else -0.5))
    return getResult(result, n_digits)

def up(val: float, n_digits: int = 0):
    val *= 10**n_digits
    result = int(val + (0.5 * (val/abs(val))))
    return getResult(result, n_digits)

def down(val: float, n_digits: int = 0):
    val *= 10**n_digits
    result = int(val - (0.5 * (val/abs(val))))
    return getResult(result, n_digits)

def halfEven(val: float, n_digits: int = 0):
    val *= 10**n_digits
    if int((val % 1)*10) == 5:
        if int((val + 1)) % 2 != 0:
            result = int(val - 0.5)
        else:
            result = int(val + 0.5)
    return getResult(result, n_digits)

def halfOdd(val: float, n_digits: int = 0):
    val *= 10**n_digits
    if int((val % 1)*10) == 5:
        if int((val + 1)) % 2 == 0:
            result = int(val + 0.5)
        else:
            result = int(val - 0.5)
    else:
        result = int(val + (0.5 if val >= 0 else -0.5))
    return getResult(result, n_digits)

finalOutput = ""


n_cases = int(input())
for _ in range(n_cases):
    line = input().rstrip()
    # change this line as needed:
    number, method, decimalPoints = [val for val in line.split(" ")]
    number, decimalPoints = (float(number), int(decimalPoints))
    if method == "HU":
        finalOutput += halfUp(number, decimalPoints)
    elif method == "HD":
        finalOutput += halfDown(number, decimalPoints)
    elif method == "U":
        finalOutput += up(number, decimalPoints)
    elif method == "D":
        finalOutput += down(number, decimalPoints)
    elif method == "HE":
        finalOutput += halfEven(number, decimalPoints)
    elif method == "HO":
        finalOutput += halfOdd(number, decimalPoints)
print(finalOutput.rstrip())
