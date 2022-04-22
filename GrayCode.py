b = int(input())


def gray(n):
    if n == 1:
        return [0, 1]

    else:
        g = gray(n - 1)
        g.extend(g[::-1])
        for i in range(len(g) // 2):
            g[i] = "0" + str(g[i])
        for i in range(len(g) // 2, len(g)):
            g[i] = "1" + str(g[i])
        return g


gl = gray(b)
for i in gl:
    print(i)