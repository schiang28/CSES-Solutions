def num(x, y):
    if x % 2 == 0:
        if y <= x:
            print(x ** 2 - y + 1)
        else:
            if y % 2 == 1:
                print(y ** 2 - x + 1)
            else:
                print((y - 1) ** 2 + x)
    else:
        if y <= x:
            print((x - 1) ** 2 + y)
        else:
            if y % 2 == 1:
                print(y ** 2 - x + 1)
            else:
                print((y - 1) ** 2 + x)


n = int(input())
for _ in range(n):
    x, y = map(int, input().split(" "))
    num(x, y)
