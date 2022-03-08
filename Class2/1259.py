numArr = []

while True:
    temp = input()
    if temp == "0":
        break
    else:
        numArr.append(temp)

for num in numArr:
    count = True
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - i - 1]:
            print("no")
            count = False
            break
    if count:
        print("yes")


