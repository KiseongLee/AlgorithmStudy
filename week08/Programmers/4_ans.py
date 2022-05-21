ans = n - len(lost)

for x in lost:
    if x in reserve:
        reserve.remove(x)
        ans += 1
    if x-1 in reserve:
        reserve.remove(x)
        ans += 1
    if x+1 in reserve:
        reserve.remove(x)
        ans += 1

return ans