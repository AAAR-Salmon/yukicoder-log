N = int(input()[-1])
M_raw = input()
if M_raw == '0':
	print(1)
	exit(0)
M = int(M_raw[-2:]) + 100
print(pow(N,M,10))
