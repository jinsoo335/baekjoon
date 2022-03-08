x, y, w, h = map(int, input().split())

vertical = 0
horizon = 0

if x >= (w - x):
    vertical = w - x
else:
    vertical = x

if y >= (h - y):
    horizon = h - y
else:
    horizon = y

print(min(vertical, horizon))

# [x, w-x, y, h-y]를 배열로 저장하고, min함수로 한번에 뽑으면 더 쉽다.