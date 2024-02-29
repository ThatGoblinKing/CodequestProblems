# https://lmcodequestacademy.com/api/static/problems/morse-code
# Need to download .in so that I can format this god-forsaken input correctly :(
EXPECTED_OUTPUT = ". . . .   .   . - . .   . - . .   - - -       . - -   - - -   . - .   . - . .   - . .\nI LOVE CODE QUEST"


n_cases = int(input())

finalOutput: str = ""
morseCodeAlphabet = {}
for _ in range(n_cases):
    for i in range(26):
        line = input().rstrip()
        morseCodeAlphabet[line[2:]] = line[0]
    morseCodeAlphabet[""] = " "
    alphabetToMorse: dict[str, str] = {v: k for k, v in morseCodeAlphabet.items()}
    alphabetToMorse[' '] = " "
    line1 = input().rstrip()
    line2 = input().rstrip()

    for character in line1:
        finalOutput += f"{alphabetToMorse[character]}   "
    finalOutput = finalOutput.rstrip() + "\n"

    for character in line2.split("   "):
        finalOutput += morseCodeAlphabet[character.lstrip()]
    finalOutput = finalOutput.rstrip() + "\n"
print(finalOutput.rstrip())
pass
