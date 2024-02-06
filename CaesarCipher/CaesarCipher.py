n_cases = int(input())
ALPH_LENGHT = 26
ALPHABET = [chr(i) for i in range(ord('a'),(ord('a') + ALPH_LENGHT))]
finalOutput = ""

for _ in range(n_cases):

    shift = int(input().rstrip())
    line = input().rstrip()
    decoder = {ALPHABET[(i + shift)%ALPH_LENGHT]:ALPHABET[i] for i in range(ALPH_LENGHT)}
    decoder[" "] = " "
    finalOutput += "".join([decoder[char] for char in line]) + "\n"

print(finalOutput.rstrip())