string = input()
finalstring=''
for i in string:
    if i.islower()==True:
        finalstring+=i.upper()
    elif i.isupper()==True:
        finalstring+=i.lower()
    else:
        finalstring+=i
print(finalstring)

