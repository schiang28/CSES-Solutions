t = int(input())
ls = []

for _ in range(t):
    a, b = list(map(int, input().split()))

    if max(a, b) // 2 > min(a, b):
        ls.append("NO")
    else:
        if (a + b) % 3 == 0:
            ls.append("YES")
        else:
            ls.append("NO")

for s in ls:
    print(s)