numlist = list(map(int,input().split(" ")))
k = int(input())
for i in range(k-1):
    numlist.remove(min(numlist))
print(min(numlist))