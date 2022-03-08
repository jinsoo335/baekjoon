N = int(input())

count3 = 0
count5 = N // 5
check = False

while count5 > 0:
    if (N - count5 * 5) % 3 == 0:
        count3 = (N - count5 * 5) // 3
        check = True
        break
    else:
        count5 -= 1

if count5 <= 0 and N % 3 == 0:
    print(N // 3)
elif not check:
    print(-1)
else:
    print(count5 + count3)
