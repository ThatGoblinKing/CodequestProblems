#https://lmcodequestacademy.com/problem/confusing-conversions
from typing import List
from contextlib import redirect_stdout
from io import StringIO

def formatHeight(line: List[str]):
    feet = int(line[0])
    inches = int(line[1])
    return f"{feet}\'{inches}\""

def formatDate(line: List[str]):
    year = int(line[0])
    month = int(line[1])
    day = int(line[2])
    return f"{year}{month:02d}{day:02d}"

def concatenate(line: List[str]):
    return ",".join(line)

f = StringIO()
with redirect_stdout(f):
    cases = int(input())
    for _ in range(cases):
        line = input()
        line = line.split(" ")
        func = line[0]
        if func == "formatHeight":
            print(formatHeight(line[1:]))
        elif func == "formatDate":
            print(formatDate(line[1:]))
        elif func == "concatenate":
            print(concatenate(line[1:]))
s = f.getvalue()
print(s.strip())