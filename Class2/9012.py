import sys

N = int(sys.stdin.readline())

for _ in range(N):
    VPS = sys.stdin.readline()
    stack = []
    check = True

    for word in VPS:
        if word == '(':
            stack.append(word)
        elif word == ')':
            if not stack:
                check = False
                break
            elif stack[-1] == '(':
                stack.pop()
            else:
                check = False
                break
    if check and (not stack):
        print("YES")
    else:
        print("NO")
