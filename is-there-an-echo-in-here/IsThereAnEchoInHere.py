# https://lmcodequestacademy.com/problem/is-there-an-echo-in-here

cases = int(input().strip())
for _ in range(cases):
    line = input().strip()

    print(f"{line}\n{line}")
