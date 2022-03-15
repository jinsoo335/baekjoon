# **는 제곱 표현, ord는 char형을

import sys

L = int(sys.stdin.readline())

sentence = list(sys.stdin.readline())

result = 0
for i in range(L):
    result += ((ord(sentence[i]) - 96) * (31 ** i))


print(result % 1234567891)
