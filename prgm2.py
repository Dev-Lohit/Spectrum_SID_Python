num=int(input())
counter=1
for i in range(2,num+1):
    counter*=i
numzero=0
while counter%10==0:
    numzero+=1
    counter = int(counter//10)
print(numzero)

    


