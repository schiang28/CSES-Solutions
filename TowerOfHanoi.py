n = int(input())
print(2 ** n - 1)


def tower(n, l, r, m):
    if n == 1:
        print(l, r)
    else:
        tower(n - 1, l, m, r)
        print(l, r)
        tower(n - 1, m, r, l)


tower(n, "1", "3", "2")