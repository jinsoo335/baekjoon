# FIFO => 큐, LIFO -> 스택 !!

from collections import deque

N = int(input())

cardDeck = deque()

for i in range(1, N + 1):
    cardDeck.append(i)

while len(cardDeck) > 1:
    cardDeck.popleft()
    if len(cardDeck) == 1:
        break
    cardDeck.append(cardDeck.popleft())

print(cardDeck[0])