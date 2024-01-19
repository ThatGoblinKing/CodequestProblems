numberOfSentences = int(input())
sentences = []
for i in range(numberOfSentences):
    sentences.append(input())
for sentence in sentences:
    numberOfVowels = 0
    for i in range (len(sentence)):
        currentChar = sentence[i]
        if currentChar == 'a' or currentChar == 'e' or currentChar == 'i' or currentChar == 'o' or currentChar == 'u':
            numberOfVowels += 1
        
    print(numberOfVowels)