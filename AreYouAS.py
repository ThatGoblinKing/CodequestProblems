numberOfWords = int(input())
words = []
for i in range(numberOfWords):
    tested = input()
    words.append(tested.split('|'))
for word in words:
    word[0], word[1] = ''.join(letter for letter in word[0].upper() if letter.isalnum()), ''.join(letter for letter in word[1].upper() if letter.isalnum())
    if word[0] == word[1]: anagram = False
    for letter in word[0]:
        word[0] = word[0].replace(letter, '', 1)
        word[1] = word[1].replace(letter, '')
    if (word[1] == ""): anagram = True
    else: anagram = False

    if anagram: result = "That's my secret contact!"
    else: result = "You're not a secret agent!"

    print(result)
    
 