from math import factorial

n = int(input())
# t = str(factorial(n))
# print(len(t) - len(t.strip("0")))

c = 0
while n >= 5:
    c += n // 5
    n = n // 5

print(c)