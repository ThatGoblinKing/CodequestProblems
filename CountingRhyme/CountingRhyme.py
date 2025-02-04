from typing import List

def is_valid_start(people : List[int], word_count: int, starting_num: int) -> bool:
    working_group = people.copy()
    if len(working_group) <= 1 or 0 not in working_group:
        return 0 in working_group

    end_person = (starting_num + (word_count - 1)) % len(working_group)
    working_group.pop(end_person)

    return is_valid_start(working_group, word_count, end_person % len(working_group))

n_cases = int(input())

for _ in range(n_cases):
    line = input().rstrip()

    group_len, words = (int(val) for val in line.split(" "))
    group = [i for i in range(group_len)]
    for i in range(group_len):
        if is_valid_start(group, words, i):
            print(i+1)
            break