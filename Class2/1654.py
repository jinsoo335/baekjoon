K, N = map(int, input().split())

cables = []

for _ in range(K):
    cables.append(int(input()))

high = max(cables)
low = 1

while low <= high:
    count = 0
    mid = (high + low) // 2
    for cable in cables:
        count += (cable // mid)

    if count >= N:
        low = mid + 1
    else:
        high = mid - 1

print(high)
