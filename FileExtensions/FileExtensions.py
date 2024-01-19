numberOfWords = int(input())
words = []
extensions = []
for i in range(numberOfWords):
    tested = input()
    words.append(tested.split('.'))
for word in words:
    if len(extensions) == 0: extensions.append([word[1], 1])
    else:
        extensionExists = False
        for extension in extensions:
            if word[1] == extension[0]: 
                extension[1] += 1
                extensionExists = True 
                break
            else: extensionExists = False
        if not extensionExists: extensions.append([word[1], 1])
for extension in extensions:
    print(extension[0], extension[1])