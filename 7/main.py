N = int(input())
isprime = [True] * (N+1)
isprime[0] = isprime[1] = False

i = 2
while i ** 2 <= N:
	if isprime[i]:
		for j in range(i*2, N+1, i):
			isprime[j] = False
	i += 1

primes = [i for i in range(N+1) if isprime[i]]

dp = [False] * (N+1)
dp[0] = dp[1] = True
for i in range(2,N+1):
	if dp[i] == True:
		continue
	dp[i] = not all(dp[i-p] for p in primes if i-p >= 0)

print('Win' if dp[N] else 'Lose')
