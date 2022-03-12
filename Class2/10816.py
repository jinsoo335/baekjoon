import sys

N = int(sys.stdin.readline())
haveCards = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
searchCards = list(map(int, sys.stdin.readline().split()))

cardsCount = dict()

for card in haveCards:
    if card in cardsCount:
        cardsCount[card] = cardsCount[card] + 1
    else:
        cardsCount[card] = 1

for card in searchCards:
    if card in cardsCount:
        print(cardsCount[card], end=' ')
    else:
        print(0, end= ' ')