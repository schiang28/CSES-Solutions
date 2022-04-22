# solution1
"""
from time import time

n = int(input())
start = time()

dp = [0 for _ in range(n + 1)]


def dice(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if dp[n] > 0:
        return dp[n]
    ans = 0
    for first in range(1, 7):
        ans += dice(n - first)
    dp[n] = ans
    return ans


print(dice(n) % 1000000007)
print(time() - start)
"""


# solution2
"""
from time import time

n = int(input())
start = time()

dp = [0 for i in range(n + 1)]
dp[0] = dp[1] = 1


for i in range(2, 7):
    if i <= n:
        dp[i] = dp[i - 1] * 2

for i in range(7, n + 1):
    dp[i] = dp[i - 1] * 2 - dp[i - 7]
    print(dp)

print(dp[n] % 1000000007)
print(time() - start)
"""


# solution3
"""
from time import time
from collections import deque

n = int(input())
start = time()

dp = deque([1, 1, 2, 4, 8, 16, 32])

if n <= 6:
    ans = dp[n]
else:
    for _ in range(n - 6):
        dp.rotate(-1)
        dp[-1] = dp[-2] * 2 - dp[-1]
        # print(dp)
    ans = dp[-1]

print(ans % 1000000007)
# print(time() - start)
"""


# solution4
"""
from time import time

n = int(input())
start = time()

dp = [1, 1, 2, 4, 8, 16, 32]

if n <= 6:
    ans = dp[n]
else:
    for _ in range(n - 6):
        x = dp.pop(0)
        dp.append(dp[-1] * 2 - x)
    ans = dp[-1]

print(ans % 1000000007)
print(time() - start)
"""

# mr gwilt's solution

from time import time

n = int(input())
start = time()
mod = 10 ** 9 + 7

dp = [0] * 6

for c in range(6):
    dp[c] = 1 + sum(dp)

c = 0
if n > 6:
    for _ in range(n - 6):
        dp[c] = sum(dp) % mod
        c = (c + 1) % 6
        # print(dp)

print(dp[(n - 1) % 6])
