#https://lmcodequestacademy.com/problem/have-you-seen-my-key
# START TIME: 9:50
# SOLVE TIME 10:04
# ELAPSED: 14MIN


cases = int(input())
for _ in range(cases):
    key_num = int(input())
    cypher_text = input()
    keys = [input() for i in range(key_num)]
    for key in keys:
        decyphered_text = ""
        for i in range(0, len(cypher_text), 2):
            num = int(cypher_text[i] + cypher_text[i + 1], 16)
            num2 = int(key[i] + key[i + 1], 16)
            decyphered_text += chr(num^num2)
        print(f"[{decyphered_text}]")