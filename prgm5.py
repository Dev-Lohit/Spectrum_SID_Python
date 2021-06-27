n = int(input())
counter = 2
while n>0:
    counter2=0
    for i in range(1,counter):
        if counter % i == 0:
            counter2 += i
    if counter2 == counter:
        print(counter,end=" ")
        n -= 1
    counter += 1
    
