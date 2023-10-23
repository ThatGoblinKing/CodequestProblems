numberOfInputs = int(input())
numbers = []
for i in range(numberOfInputs):
    numbers.append(input().split(' '))
for number in numbers:
    num1 = float(number[0])
    num2 = float(number[1])
    num3 = float(number[2])
    
    num1 -= 180
    num2 -= 180
    num3 -= 180
    
    if num1 < 0: num1 += 360
    if num2 < 0: num2 += 360
    if num3 < 0: num3 += 360
    
    print(f"{num1:0>6.2f} {num2:0>6.2f} {num3:0>6.2f}")
    