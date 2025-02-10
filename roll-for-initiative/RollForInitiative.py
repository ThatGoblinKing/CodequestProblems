#https://lmcodequestacademy.com/problem/roll-for-initiative

from contextlib import redirect_stdout
from io import StringIO


# PRIORITY OF ABILITY SCORES
# NUMBERS WE ASSIGN TO THEM

def main():
    cases = int(input())
    for _ in range(cases):
        line = input()
        class_num, player_num = (int(val) for val in line.split(" "))
        class_dict = {}
        for i in range(class_num):
            line = input()
            input_list = line.split(" ")
            class_dict[input_list[0]] = input_list[1:]
        for i in range(player_num):
            line = input()
            input_list = line.split(" ")
            class_name = input_list[0]
            input_list.pop(0)
            input_list = [int(val) for val in input_list]
            input_list.sort(reverse=True)
            player_dict = {}
            for j in range(len(input_list)):
                player_dict[class_dict[class_name][j]] = input_list[j]
            print(f"""{class_name}
STR: {player_dict["STR"]}
DEX: {player_dict["DEX"]}
CON: {player_dict["CON"]}
INT: {player_dict["INT"]}
WIS: {player_dict["WIS"]}
CHA: {player_dict["CHA"]}""")
            
f = StringIO()
with redirect_stdout(f):
    main()
s = f.getvalue()
print(s.strip())