#https://lmcodequestacademy.com/problem/reflection
from contextlib import redirect_stdout
from io import StringIO


def main():
    cases = int(input())
    for _ in range(cases):
        img_lines = int(input())
        img_list = [""] * img_lines
        for i in range(img_lines):
            img_list[i] = input()
        reflect_choice = input()
        if reflect_choice == "X":
                img_list = img_list[::-1]
        elif reflect_choice == "Y":
                img_list = [line[::-1] for line in img_list]
        elif reflect_choice == "INVERSE":
                longest_line = max(img_list, key=len)
                inverted_list = [[" " for i in range(img_lines)] for i in range (len(longest_line))]
                for j in range(img_lines):
                    for k in range(len(img_list[j])):
                        inverted_list[k][j] = img_list[j][k]
                img_list = ["".join(line) for line in inverted_list]
                # img_list =
        print("\n".join(img_list))
        # print(img_list)
        
f = StringIO()

with redirect_stdout(f):
    main()
s = f.getvalue()

with open("reflection\out.txt", 'r') as file:
    EXPECTED_OUTPUT = file.read()

print(s)