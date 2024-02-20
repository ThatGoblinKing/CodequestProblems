from string import ascii_uppercase as ALPHABET

n_cases = int(input())
for _ in range(n_cases):
    toEncode = input().rstrip()
    keyword = input().rstrip()

    alphabets = []

    for character in keyword:
        currentCodeCharacter = ALPHABET.index(character)
        encodedAlphabet = ALPHABET[currentCodeCharacter:] + ALPHABET[:currentCodeCharacter]
        alphabets.append(encodedAlphabet)

    encodedWord = ""
    offset = 0

    for i in range(len(toEncode)):
        if toEncode[i] == " ":
            encodedWord += " "
            offset += 1
        else:
            encodeIndex = ALPHABET.index(toEncode[i])
            encodedCharacter = alphabets[(i-offset)%len(alphabets)][encodeIndex]
            encodedWord += encodedCharacter
    print(encodedWord.rstrip())

# list of characters
# alphabet[0] = a so on so forth
# Start alphabet at letter of codeword, add any leading letters to the end
# encodedAlphabet = alphabet[index of letter:] + alphabet[:index of letter]

# HOW DO WE FIND INDICES??????
# alphabet.index(character)

# unencodedWord = Lockheed
# encodeIndex = alphabet.index(unencodedWord[0])

# encodedCharacter = encodedAlphabet[encodeIndex]