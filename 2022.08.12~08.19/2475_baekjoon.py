X = list(map(int, input().split()))

checknum = 0
for a in X:
    checknum += a**2

print(checknum%10)

# 제곱수 체크 m**n