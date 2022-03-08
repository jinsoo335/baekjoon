N = input()

digit = len(N)

N = int(N)
check = False

if N > 27:
    for i in range(N - (9 * digit), N):
        divinSum = i
        for j in str(i):
            divinSum += int(j)

        if divinSum == N:
            print(i)
            check = True
            break
else:
    for i in range(1, N):
        divinSum = i
        for j in str(i):
            divinSum += int(j)

        if divinSum == N:
            print(i)
            check = True
            break


if not check:
    print(0)