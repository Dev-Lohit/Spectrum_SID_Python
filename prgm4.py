numlist = list(map(int,input().split(" ")))
counterlist = []
for n in numlist:
    for k in range (1,n+1):
        if n % k == 0:
            counterlist.append(k)
counterlist2=[]
for g in counterlist:
    if counterlist.count(g)==len(numlist):
        counterlist2.append(g)
        counterlist.remove(g)
print(max(counterlist2))
