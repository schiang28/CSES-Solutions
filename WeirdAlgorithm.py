n = int(input())

if n == 1:
    print(1)

count = 0
while n > 1:
    if count == 0:
        print(n, end=" ")
    if n % 2 == 0:
        n /= 2
    else:
        n = n*3+1
    print(int(n), end=" ")
    count += 1
