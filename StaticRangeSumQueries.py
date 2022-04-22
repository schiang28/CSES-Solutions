n, q = map(int, input().split())
num = list(map(int, input().split()))

g = [0] * (len(num) + 1)

for i in range(len(num)):
    g[i + 1] = g[i] + num[i]

for _ in range(q):
    a, b = map(int, input().split())
    print(g[b] - g[a - 1])
