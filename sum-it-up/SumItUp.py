#https://lmcodequestacademy.com/problem/sum-it-up

cases = int(input())
for _ in range(cases):
    line = input()
    val1, val2 = (int(val) for val in line.split(" "))
    sum = val1 + val2
    print(sum * 2 if val1 == val2 else sum)