testCases = int(input()); outputLine = ""; EXPECTED_OUTPUT = '44-33-555-555-666-0-9-666-777-555-3\n555-666-222-55-44-33-33-3-0-6-2-777-8-444-66\n222-666-3-33-0-77-88-33-7777-8';LETTERS = {'A':"2", 'B':"22", 'C':"222", 'D':"3", 'E':"33", 'F':"333", 'G':"4", 'H':"44", 'I':"444", 'J':"5", 'K':"55", 'L':"555", 'M':"6", 'N':"66", 'O':"666", 'Z':'9999', 'Y':'999', 'X':'99', 'W':'9', 'V':'888', 'U':'88', 'T':'8', 'S':'7777', 'R':'777', 'Q':'77', 'P':'7', ' ':"0"}
for case in range(testCases): 
    line = input().rstrip().upper()
    for character in line:outputLine += f"{LETTERS[character]}-"; outputLine = outputLine[:-1] + "\n"
print(outputLine.rstrip())