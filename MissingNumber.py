x=int(input())
y=list(map(int, input().split()))

num=list(range(1,x+1))
print(sum(num)-sum(y))