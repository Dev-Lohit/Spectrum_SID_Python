counter = 5
for n in range(9):
    if n < 5:
        print((" "*n)+("* "*counter))
        counter -= 1
    else:
        print((" "*(9-n-1))+("* "*(counter+2)))
        counter+=1
        