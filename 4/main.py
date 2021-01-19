N = int(input())
W = map(int,input().split())

dp = [False] * 10001
dp[0] = 1
sum = 0
for w in W:
	sum += w
	for i in range(10000, -1, -1):
		if dp[i]:
			dp[i+w] = True
print('possible' if sum % 2 == 0 and dp[sum // 2] else 'impossible')
