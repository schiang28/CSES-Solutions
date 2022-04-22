n = int(input())
num = list(range(1, n + 1))
s1, s2 = [], []

if n % 4 == 0:
    print("YES")
    x = n // 4
    s1.extend(num[:x])
    s1.extend(num[-x:])
    s2.extend(num[x:-x])
    print(len(s1))
    print(*s1)
    print(len(s2))
    print(*s2)
elif n % 4 == 3:
    print("YES")
    s1.append(n)
    for i in range((n - 1) // 2):
        if i % 2 == 1:
            s1.append(num[i])
            s1.append(num[-i - 2])
        else:
            s2.append(num[i])
            s2.append(num[-i - 2])
    print(len(s1))
    print(*s1)
    print(len(s2))
    print(*s2)
else:
    print("NO")