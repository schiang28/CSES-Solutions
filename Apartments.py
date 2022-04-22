"""
n, m, k = list(map(int, input().split(" ")))
desired_size = sorted(list(map(int, input().split(" "))))
actual_size = sorted(list(map(int, input().split(" "))))

# print(desired_size)
# print(actual_size)

count = 0
for i in desired_size:
    for j in actual_size:
        if i - k <= j <= i + k:
            count += 1
            actual_size.remove(j)
            break

print(count)
"""

f = lambda: map(int, input().split())
n, m, k = f()
a = sorted(f())
b = sorted(f())

i, j, c = 0, 0, 0

while i < n and j < m:
    if a[i] + k < b[j]:
        i += 1
    elif a[i] - k > b[j]:
        j += 1
    else:
        i += 1
        j += 1
        c += 1
print(c)