y=int(input())
x=list(map(int, input().split()))

moves = 0
for i in range(1,y):
    if x[i]>=x[i-1]:
        continue
    else:
        diff = (x[i-1]-x[i])
        x[i]+= diff
        moves+=diff

print(moves)