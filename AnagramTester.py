numberOfWords = int(input())
words = []
for i in range(numberOfWords):
    tested = input()
    words.append(tested.split('|'))
for word in words:
    testedWords = word[0] + "|" + word[1]
    if word[0] == word[1]: anagram = False
    elif (len(word[0]) == len(word[1])):
        for letter in word[0]:
            word[0] = word[0].replace(letter, '', 1)
            word[1] = word[1].replace(letter, '', 1)
    else: anagram = (False)
    if (word[1] == ""): anagram = True
    else: anagram = False

    if anagram: result = "ANAGRAM"
    else: result = "NOT AN ANAGRAM"

    print(f"{testedWords} = {result}", end = '\n')
    
 