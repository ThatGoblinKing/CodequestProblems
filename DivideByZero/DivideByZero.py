def better_round(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return result / 10**n_digits


testCases = int(input())
for case in range(testCases):
    line = input().rstrip()


    # change this line as needed:
    dividend, divisor = (val for val in line.split(" "))
    try:
        dividend = float(dividend)
    except:
        print("Invalid Dividend")
        continue
    try:
        divisor = float(divisor)
    except:
        print("Invalid Divisor")
        continue
    try:
        print(f"{better_round(dividend/divisor, 1):.01f}")
    except:
        print("Divide By Zero")