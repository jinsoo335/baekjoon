# 체스판의 시작 지점이 W인지 B인지에 따라 다른 갯수가 나오기 때문에
# count 배열에 각 8*8 체스판에 따라 2개씩의 개수를 넣는다.

N, M = map(int, input().split())

origin = []     # 받을 배열
count = []      # 몇번 바꿀지를 샐 배열

for _ in range(N):
    origin.append(input())

for i in range(N - 7):  # -7을 하는 이유는 만약 8일 경우 1이 되어 한번만 돌기에..
    for j in range(M - 7):  # 만약 8을 넘은 수들에 대해서는 -7을 하면 그만큼의 체스판 개수가 나온다.
        num1 = 0            # 만약 9인 경우 -7을 하면 2 => 8*8 체스판이 2개가 나올 수 있다.
        num2 = 0
        for a in range(i, i + 8):   #i 부터 i + 7까지 8줄을 체크한다.
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:    # 행과 열의 합이 짝수일 경우 시작점과 같아야 한다.
                    if origin[a][b] != 'W':     # num1은 시작점이 W인 경우를 체크, num2는 시작점이 B인 경우를 체크
                        num1 += 1               # num1의 경우 행-열의 합이 짝수면 W여야 한다, W가 아니면 한번 바꿀 필요가 있다.
                    else:                       # num2의 경우 행-열의 합이 짝수면 B여야 한다, W인 경우 바꿀 필요가 있다.
                        num2 += 1
                else:                   # 행과 열의 합이 홀수인 경우 시작점과 달라야 한다.
                    if origin[a][b] != 'B':     # num1의 경우 행-열의 합이 홀수면 B여야 한다. B가 아니면 한번 바꿀 필요가 있다.
                        num1 += 1               # num2의 경우 행-열의 합이 홀수면 W여야 한다. W가 아니면 한번 바꿀 필요하 있다.
                    else:
                        num2 += 1
        count.append(num1)          # 두 결과를 더한다.
        count.append(num2)
print(min(count))   # 모든 경우의 수들 중에서 제일 작은 수를 하나 뽑는다.