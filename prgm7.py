numlist = list(map(int,input().split(" ")))
n=int(input())
anytriplet=False
for j in range(len(numlist)-2):
    for k in range(j+1,len(numlist)-1):
        if anytriplet==False:
            for t in range(j+2,len(numlist)):
                if numlist[j]+numlist[k]+numlist[t]==n:
                    print(numlist[j],numlist[k],numlist[t])
                    anytriplet=True
if anytriplet==False:
    print("No triplet")
