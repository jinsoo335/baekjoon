N = int(input())

numAry = []
printAry = []
point = 0

for _ in range(N):
    num = int(input())

    if not numAry:
        for i in range(point + 1, num + 1):
            numAry.append(i)
            printAry.append("+")
        point = num

    if numAry and (numAry[-1] > num):
        point = -1
        break

    if numAry[-1] < num:
        for i in range(point + 1, num + 1):
            numAry.append(i)
            printAry.append("+")
        point = num

    if numAry[-1] == num:
        numAry.pop()
        printAry.append("-")


if point == -1:
    print("NO")
else:
    for sign in printAry:
        print(sign)