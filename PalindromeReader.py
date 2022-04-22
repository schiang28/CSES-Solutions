n = input()

odd = []
even = []
for char in set(n):
    if n.count(char) % 2 == 1:
        odd.append(char)
        if n.count(char) > 1:
            for _ in range(n.count(char) // 2):
                even.append(char)
    else:
        for _ in range(n.count(char) // 2):
            even.append(char)

if len(n) % 2 == 1:
    if len(odd) > 1:
        print("NO SOLUTION")
    else:
        print("".join(even) + odd[0] + "".join(even[::-1]))
else:
    if len(odd) > 0:
        print("NO SOLUTION")
    else:
        print("".join(even) + "".join(even[::-1]))

# print(even)
# print(odd)