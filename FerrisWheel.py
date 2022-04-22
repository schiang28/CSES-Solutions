f = lambda: map(int, input().split())
n, x = f()
w = sorted(f())
c = 0

while len(w) > 0:
    for i in w[::-1][:-1]:
        if w[0] + i <= x:
            w.remove(i)
            break
    del w[0]
    c += 1

print(c)

"""n = [int(i) for i in input().split()]
ls = [int(i) for i in input().split()]

ls.sort()

j = n[0] - 1
c, i = 0, 0

while i <= j:
    if ls[i] + ls[j] > n[1]:
        j -= 1
    else:
        i += 1
        j -= 1
    c += 1

print(c)"""
