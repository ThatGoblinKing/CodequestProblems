from string import ascii_lowercase as alphabet

#https://lmcodequestacademy.com/problem/encryption
finalOutput = []
cases = int(input())
for _ in range(cases):
    cipherKey = {}
    line = input()
    encrypting = (line == "ENCRYPT")
    line = input()
    for i in range(len(alphabet)):
        cipherKey[alphabet[i]] = line[i]
    if not encrypting:
        values = list(cipherKey.values())
        keys = list(cipherKey.keys())
        for i in range(len(cipherKey.values())):
            cipherKey[values[i]] = keys[i]
    for i in range(int(input())):
        currentWord = ""
        for character in (input()):
            if character == " ":
                currentWord += " "
                continue
            capitalized = character.isupper()
            currentWord += cipherKey[character.lower()].upper() if capitalized else cipherKey[character.lower()]
        finalOutput.append(currentWord)
print("\n".join(finalOutput))