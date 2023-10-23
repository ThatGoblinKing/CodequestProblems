numberOfNumbers = int(input())
numbers = []
for i in range(numberOfNumbers):
    numbers.append(int(input()))
for number in numbers:
   if number / abs(number) == -1: print("NEGATIVE")
   else: print("POSITIVE")