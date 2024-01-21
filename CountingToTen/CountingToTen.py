testCases = int(input())
for case in range(testCases):
    line = int(input().rstrip())
    print("\n".join([f"{i:>0{line}b}".format(i) for i in range(2**line)]))