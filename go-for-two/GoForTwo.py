#https://lmcodequestacademy.com/problem/go-for-two

cases = int(input())
for _ in range(cases):
    line = input()
    val1, val2 = (float(val) for val in line.split(" "))