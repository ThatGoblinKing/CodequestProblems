#https://lmcodequestacademy.com/problem/animal-farm

cases = int(input())
for _ in range(cases):
    line = input()
    val1, val2, val3 = (int(val) for val in line.split(" "))
    print(f"{val1 * 2 + val2 * 4 + val3 * 4}")