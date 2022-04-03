t = int(input())

for i in range(t):
    r, s = input().split()

    r = int(r)

    for i in s:
        print(f'{i}'*r, end="")
    print()