numberOfInputs = int(input())
numbers = []
for i in range(numberOfInputs):
    numbers.append(input())
for number in numbers:
    num1, num2 = number.split(' ')
    print(f"{int(num1) + int(num2)} {int(num1) * int(num2)}")