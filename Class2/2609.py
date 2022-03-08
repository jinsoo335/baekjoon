# 유클리드 호제법..
a, b = map(int, input().split())

a, b = max(a, b), min(a, b)
# 최대공약수
# 두 자연수 a, b의 최대 공약수는 b와 a % b의 최대공약수와 같다
# a, b = b, a % b # 위의 성질을 나누는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a, b의 최대공약수이다.
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수는 두 수의 곱 나누기 최대공약수..
def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))
