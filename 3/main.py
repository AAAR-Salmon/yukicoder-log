import sys
import math
from math import sin, cos, tan
from functools import reduce
from collections import deque
import heapq
sys.setrecursionlimit(1000000)
intm1 = lambda x:int(x)-1

def popcount(x):
	assert(0 <= x <= 0xFFFFFFFF)
	x = x - (x >> 1 & 0x55555555)
	x = (x & 0x33333333) + (x >> 2 & 0x33333333)
	x = (x + (x >> 4)) & 0x0f0f0f0f
	x = (x + (x >> 8)) & 0x00ff00ff
	x = (x + (x >> 16)) & 0x0000ffff
	return x

N = int(input())
dp = [-1] * (N + 1)
dp[1] = 1
q = deque([1])
while q:
	c = q.popleft()
	d = popcount(c)
	for mv in [d, -d]:
		if 1 <= c+mv <= N and dp[c+mv] == -1:
			dp[c+mv] = dp[c] + 1
			q.append(c+mv)
print(dp[N])
