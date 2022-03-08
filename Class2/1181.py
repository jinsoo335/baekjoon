N = int(input())

wordList = []

for _ in range(N):
    wordList.append(input())

wordList.sort()
sortedWordList = []

for i in range(1, 51):
    prev = " "
    for word in wordList:
        if (len(word) == i) & (prev != word):
            sortedWordList.append(word)
            prev = word

prev = ""
for word in sortedWordList:
    if prev != word:
        print(word)
        prev = word