n = int(input())
for i in range(2, n+1):
	div = 2
	while div < i:
		if i % div == 0:
			break
		else:
			div+=1
	if div == i:
		print(i,end=" ")