L = int(input())
N = int(input())
W = sorted(map(int,input().split()))

ans = 0
for w in W:
	if L >= w:
		L -= w
		ans += 1

print(ans)
